from amadeus import Client, ResponseError
from datetime import datetime
import os
import requests
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize Amadeus client
amadeus = Client(
    client_id=st.secrets["AMADEUS_API_KEY"],
    client_secret=st.secrets["AMADEUS_SECRET_KEY"]
)

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def geocode_place(place_name):
    """Get coordinates for a place using Nominatim"""
    url = "https://nominatim.openstreetmap.org/search"
    headers = {"User-Agent": "TravelBuddy/1.0"}
    params = {
        "q": place_name,
        "format": "json",
        "limit": 1
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data:
                return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception as e:
        st.error(f"Geocoding error: {str(e)}")
    return None

def get_nearest_airport(city_name):
    """Enhanced airport finder combining geocoding and Amadeus API"""
    if not city_name or not isinstance(city_name, str):
        return None
    
    city_name = city_name.lower().strip()
    
    # First try direct airport lookup
    try:
        response = amadeus.reference_data.locations.get(
            keyword=city_name,
            subType='AIRPORT',
            view='LIGHT'
        )
        if response.data:
            # Filter to only airports with IATA codes
            valid_airports = [a for a in response.data if 'iataCode' in a]
            if valid_airports:
                return valid_airports[0]['iataCode']
    except Exception as e:
        st.warning(f"Direct airport lookup failed for {city_name}: {str(e)}")

    # If no direct airport found, try geocoding + nearby airports
    coords = geocode_place(city_name)
    if coords:
        lat, lon = coords
        try:
            airports = amadeus.reference_data.locations.airports.get(
                latitude=lat,
                longitude=lon,
                radius=300  # 300 km radius
            ).data

            if airports:
                # Filter airports with IATA codes and sort by distance
                valid_airports = [a for a in airports if 'iataCode' in a]
                if valid_airports:
                    sorted_airports = sorted(
                        valid_airports,
                        key=lambda x: float(x['distance']['value'])
                    )
                    return sorted_airports[0]['iataCode']
        except Exception as e:
            st.warning(f"Nearby airport search failed for {city_name}: {str(e)}")

    # Fallback to major airports if nothing found
    major_indian_airports = {
        'delhi': 'DEL', 'mumbai': 'BOM', 'bangalore': 'BLR',
        'chennai': 'MAA', 'kolkata': 'CCU', 'hyderabad': 'HYD',
        'pune': 'PNQ', 'ahmedabad': 'AMD', 'jaipur': 'JAI'
    }
    
    # Check for exact city matches first
    if city_name in major_indian_airports:
        return major_indian_airports[city_name]
    
    # Check for partial matches
    for city, code in major_indian_airports.items():
        if city in city_name:
            return code

    # Ultimate fallback to Delhi
    return 'DEL'

def get_alternative_airports(city_name, exclude=None):
    """Get nearby airports within 300km radius of a city"""
    exclude = exclude or []
    alternatives = []
    
    # First try geocoding the city
    coords = geocode_place(city_name)
    if not coords:
        return alternatives
    
    lat, lon = coords
    
    try:
        # Search for airports within 300km radius
        response = amadeus.reference_data.locations.airports.get(
            latitude=lat,
            longitude=lon,
            radius=300  # 300 km radius
        )
        
        if response.data:
            # Filter valid airports not in exclude list
            valid_airports = [
                a for a in response.data 
                if 'iataCode' in a and a['iataCode'] not in exclude
            ]
            
            # Sort by distance (nearest first)
            valid_airports.sort(key=lambda x: float(x['distance']['value']))
            
            # Return just the IATA codes (max 5 alternatives)
            alternatives = [a['iataCode'] for a in valid_airports[:5]]
            
    except ResponseError as e:
        st.warning(f"Airport search error for {city_name}: {str(e)}")
    except Exception as e:
        st.warning(f"Unexpected error finding airports for {city_name}: {str(e)}")
    
    return alternatives

def flight_planner_agent(origin_city, destination_city, departure_date, return_date, adults=1):
    """
    Complete flight search with automatic fallback to nearby airports (destination only)
    """
    try:
        # ===== 1. VALIDATION =====
        if not all([origin_city, destination_city, departure_date, return_date]):
            st.error("❌ Please fill all search fields")
            return False

        try:
            dep_dt = datetime.strptime(departure_date, '%Y-%m-%d').date()
            ret_dt = datetime.strptime(return_date, '%Y-%m-%d').date()
            if dep_dt >= ret_dt:
                st.error("❌ Return date must be after departure date")
                return False
            if dep_dt < datetime.now().date():
                st.error("❌ Departure date cannot be in the past")
                return False
        except ValueError:
            st.error("❌ Invalid date format (use YYYY-MM-DD)")
            return False

        if not isinstance(adults, int) or adults < 1 or adults > 9:
            st.error("❌ Adults must be 1-9")
            return False

        # ===== 2. AIRPORT LOOKUP =====
        with st.spinner("📍 Finding nearest airports..."):
            # Get primary airports - only look for alternatives for destination
            origin_code = get_nearest_airport(origin_city.strip())
            dest_code = get_nearest_airport(destination_city.strip())

            if not origin_code:
                st.error(f"❌ No airport found near: {origin_city}")
                return False
            if not dest_code:
                st.error(f"❌ No airport found near: {destination_city}")
                return False

            st.info(f"Departure from: {origin_code} (Nearest to {origin_city})")
            st.info(f"Arrival at: {dest_code} (Nearest to {destination_city})")

            # Get alternative airports only for destination (within 300km radius)
            dest_alternatives = get_alternative_airports(destination_city, exclude=[dest_code])

        # ===== 3. FLIGHT SEARCH WITH FALLBACK =====
        all_offers = []
        airports_tried = set()

        # Try different destination airports (keep origin fixed)
        for destination in [dest_code] + dest_alternatives[:3]:  # Primary + 3 nearest alternatives
            if (origin_code, destination) in airports_tried:
                continue
            
            airports_tried.add((origin_code, destination))
            
            with st.spinner(f"🔍 Searching {origin_code}→{destination}..."):
                try:
                    params = {
                        'originLocationCode': origin_code,
                        'destinationLocationCode': destination,
                        'departureDate': departure_date,
                        'returnDate': return_date,
                        'adults': adults,
                        'currencyCode': 'INR',
                        'max': 5
                    }
                    response = amadeus.shopping.flight_offers_search.get(**params)
                    if response.data:
                        # Add airport info to each offer
                        for offer in response.data:
                            offer['_search_info'] = {
                                'origin_airport': origin_code,
                                'dest_airport': destination,
                                'is_primary': (destination == dest_code)
                            }
                        all_offers.extend(response.data)
                        
                        # If we found primary airport flights, stop searching alternatives
                        if destination == dest_code and len(response.data) >= 3:
                            break
                except Exception as e:
                    st.warning(f"Search failed for {origin_code}→{destination}: {str(e)}")
            
            # If we have enough primary airport offers, stop
            primary_count = len([o for o in all_offers if o['_search_info']['is_primary']])
            if primary_count >= 3:
                break

        # ===== 4. DISPLAY RESULTS =====
        if not all_offers:
            st.warning(f"""
            🛫 No flights found for:
            • {origin_city} → {destination_city}
            • {dep_dt.strftime('%b %d')} - {ret_dt.strftime('%b %d %Y')}
            """)
            
            # Show alternative airports we tried
            if len(airports_tried) > 1:
                st.info("ℹ️ Also tried these alternative destination airports:")
                cols = st.columns(4)
                for i, (orig, dest) in enumerate(airports_tried):
                    if dest != dest_code:
                        cols[i%4].write(f"{dest}")
            return True

        # Sort offers - primary airport results first, then by price
        all_offers.sort(key=lambda x: (
            not x['_search_info']['is_primary'],
            float(x['price']['total'])
        ))

        primary_offers = [o for o in all_offers if o['_search_info']['is_primary']]
        alternate_offers = [o for o in all_offers if not o['_search_info']['is_primary']]

        if primary_offers:
            st.success(f"✨ Found {len(primary_offers)} flight options to {dest_code}")
        if alternate_offers:
            st.info(f"💡 Also found {len(alternate_offers)} options to alternative airports")

        # Initialize selection state
        if 'selected_flight' not in st.session_state:
            st.session_state.selected_flight = None
        st.session_state.travel_data = st.session_state.get('travel_data', {})
        st.session_state.travel_data['flight_cost'] = None

        # Display all flight options
        for i, offer in enumerate(all_offers, 1):
            price = int(float(offer['price']['total']))
            outbound = offer['itineraries'][0]
            return_trip = offer['itineraries'][1] if len(offer['itineraries']) > 1 else None
            
            # Get airport codes from search info
            origin_airport = offer['_search_info']['origin_airport']
            dest_airport = offer['_search_info']['dest_airport']
            
            # Outbound flight details
            dep_seg = outbound['segments'][0]
            dep_time = datetime.strptime(dep_seg['departure']['at'], '%Y-%m-%dT%H:%M:%S')
            airline = dep_seg['carrierCode']
            flight_num = f"{airline}{dep_seg['number']}"
            arr_seg = outbound['segments'][-1]
            arr_time = datetime.strptime(arr_seg['arrival']['at'], '%Y-%m-%dT%H:%M:%S')
            duration = outbound['duration'].replace('PT','').replace('H','h ').replace('M','m').strip()
            stops = len(outbound['segments']) - 1

            with st.container():
                # Show airport indicator if using alternatives
                if not offer['_search_info']['is_primary']:
                    st.caption(f"🚩 Alternative destination airport: {dest_airport}")
                
                st.markdown(f"### {airline} • {flight_num}")
                
                # Outbound flight
                st.markdown(f"#### 🛫 Outbound: {dep_time.strftime('%a, %b %d')}")
                col1, col2, col3 = st.columns([3, 2, 3])
                with col1:
                    st.caption("FROM")
                    st.markdown(f"**{origin_airport}**")
                    st.write(dep_time.strftime('%H:%M'))
                with col2:
                    st.caption("DURATION")
                    st.write(duration)
                    st.write("→")
                    st.caption(f"{stops} STOP{'S' if stops != 1 else ''}")
                with col3:
                    st.caption("TO")
                    st.markdown(f"**{dest_airport}**")
                    st.write(arr_time.strftime('%H:%M'))

                # Return flight if available
                if return_trip:
                    return_dep_seg = return_trip['segments'][0]
                    return_dep_time = datetime.strptime(return_dep_seg['departure']['at'], '%Y-%m-%dT%H:%M:%S')
                    st.markdown(f"#### 🛬 Return: {return_dep_time.strftime('%a, %b %d')}")
                    return_airline = return_dep_seg['carrierCode']
                    return_flight_num = f"{return_airline}{return_dep_seg['number']}"
                    return_arr_seg = return_trip['segments'][-1]
                    return_arr_time = datetime.strptime(return_arr_seg['arrival']['at'], '%Y-%m-%dT%H:%M:%S')
                    return_duration = return_trip['duration'].replace('PT','').replace('H','h ').replace('M','m').strip()
                    return_stops = len(return_trip['segments']) - 1

                    col1, col2, col3 = st.columns([3, 2, 3])
                    with col1:
                        st.caption("FROM")
                        st.markdown(f"**{dest_airport}**")
                        st.write(return_dep_time.strftime('%H:%M'))
                    with col2:
                        st.caption("DURATION")
                        st.write(return_duration)
                        st.write("→")
                        st.caption(f"{return_stops} STOP{'S' if return_stops != 1 else ''}")
                    with col3:
                        st.caption("TO")
                        st.markdown(f"**{origin_airport}**")
                        st.write(return_arr_time.strftime('%H:%M'))

                st.markdown(f"### Total Price: ₹{price:,}")

                if st.button(f"Select This Flight", key=f"select_{i}_{origin_airport}_{dest_airport}"):
                    flight_data = {
                        'number': i,
                        'price': price,
                        'airline': airline,
                        'flight_number': flight_num,
                        'departure': {
                            'airport': origin_airport,
                            'city': origin_city,
                            'time': dep_time.strftime('%H:%M'),
                            'date': dep_time.strftime('%Y-%m-%d'),
                            'datetime': dep_time.strftime('%a, %b %d %H:%M')
                        },
                        'arrival': {
                            'airport': dest_airport,
                            'city': destination_city,
                            'time': arr_time.strftime('%H:%M'),
                            'date': arr_time.strftime('%Y-%m-%d'),
                            'datetime': arr_time.strftime('%a, %b %d %H:%M')
                        },
                        'duration': duration,
                        'stops': stops,
                        'offer': offer
                    }
                    
                    if return_trip:
                        flight_data['return_flight'] = {
                            'airline': return_airline,
                            'flight_number': return_flight_num,
                            'departure': {
                                'airport': dest_airport,
                                'city': destination_city,
                                'time': return_dep_time.strftime('%H:%M'),
                                'date': return_dep_time.strftime('%Y-%m-%d'),
                                'datetime': return_dep_time.strftime('%a, %b %d %H:%M')
                            },
                            'arrival': {
                                'airport': origin_airport,
                                'city': origin_city,
                                'time': return_arr_time.strftime('%H:%M'),
                                'date': return_arr_time.strftime('%Y-%m-%d'),
                                'datetime': return_arr_time.strftime('%a, %b %d %H:%M')
                            },
                            'duration': return_duration,
                            'stops': return_stops
                        }
                    
                    st.session_state.selected_flight = flight_data
                    st.session_state.travel_data['flight_cost'] = price
                    st.rerun()

        if st.session_state.selected_flight:
            return st.session_state.selected_flight

        return None

    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return False