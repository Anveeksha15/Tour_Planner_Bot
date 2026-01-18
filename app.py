import streamlit as st
st.cache_data.clear()
from datetime import datetime, timedelta, timezone
from agents.budget_agent import calculate_budget
from agents.destination_agent import destination
from agents.flight_planner import flight_planner_agent
from agents.itenary_agent import generate_itinerary
from agents.weather_agent import weather_forecast
import time
import re

# Set page config
st.set_page_config(
    page_title="Travel Buddy - Your Smart Travel Assistant",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Color Scheme
PRIMARY_COLOR = "#1E3A8A"      # Deep Blue
SECONDARY_COLOR = "#14B8A6"    # Teal
ACCENT_COLOR = "#F97316"       # Vibrant Orange
BACKGROUND_COLOR = "#0F172A"   # Midnight Navy
TEXT_COLOR = "#FFFFFF"         # Pure White
SUCCESS_COLOR = "#22C55E"      # Green
INFO_COLOR = "#38BDF8"         # Sky Blue
WARNING_COLOR = "#FACC15"      # Golden Yellow
ERROR_COLOR = "#EF4444"    

# Custom CSS
st.markdown(f"""
<style>
    .stApp {{
        background-color: {BACKGROUND_COLOR};
    }}
    .sidebar .sidebar-content {{
        background: linear-gradient(180deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        color: white;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {TEXT_COLOR} !important;
        font-family: 'Inter', sans-serif;
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white !important;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: {SECONDARY_COLOR};
        transform: scale(1.02);
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    .card {{
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #E5E7EB;
    }}
    .success-card {{
        border-left: 4px solid {SUCCESS_COLOR};
        background-color: rgba(16, 185, 129, 0.05);
    }}
    .info-card {{
        border-left: 4px solid {INFO_COLOR};
        background-color: rgba(59, 130, 246, 0.05);
    }}
    .warning-card {{
        border-left: 4px solid {WARNING_COLOR};
        background-color: rgba(245, 158, 11, 0.05);
    }}
    .step-indicator {{
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        padding: 0.75rem;
        border-radius: 8px;
        background-color: rgba(37, 99, 235, 0.1);
    }}
    .step-indicator.active {{
        background-color: rgba(37, 99, 235, 0.2);
        font-weight: 600;
    }}
    .step-indicator.completed {{
        background-color: rgba(16, 185, 129, 0.1);
    }}
    .step-number {{
        background-color: {PRIMARY_COLOR};
        color: white;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 12px;
        font-weight: bold;
    }}
    .step-number.completed {{
        background-color: {SUCCESS_COLOR};
    }}
    .step-number.active {{
        background-color: {SECONDARY_COLOR};
    }}
</style>
""", unsafe_allow_html=True)

# App header
st.markdown(f"""
<div style="background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
            padding: 2rem;
            border-radius: 12px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <h1 style="color: white; margin: 0;">✈️ Travel Buddy</h1>
    <h3 style="color: white; margin: 0; font-weight: normal;">Your Smart Travel Planning Assistant</h3>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'travel_data' not in st.session_state:
    st.session_state.travel_data = {}
if 'destinations' not in st.session_state:
    st.session_state.destinations = []
if 'destination_details' not in st.session_state:
    st.session_state.destination_details = {}

# Sidebar - Progress tracker
with st.sidebar:
    st.markdown(f"""
    <div style="background: {SECONDARY_COLOR};
                padding: 1rem;
                border-radius: 12px;
                color: white;
                margin-bottom: 1.5rem;">
        <h3 style="color: white; margin: 0;">Your Travel Plan Progress</h3>
    </div>
    """, unsafe_allow_html=True)
    
    steps = {
        1: "Trip Preferences",
        2: "Destination Selection",
        3: "Flight Options",
        4: "Budget Planning",
        5: "Itinerary",
        6: "Weather Forecast"
    }
    
    for step_num, step_name in steps.items():
        is_completed = step_num < st.session_state.current_step
        is_active = step_num == st.session_state.current_step
        
        step_class = ""
        number_class = ""
        if is_active:
            step_class = "active"
            number_class = "active"
        elif is_completed:
            step_class = "completed"
            number_class = "completed"
        
        st.markdown(f"""
        <div class="step-indicator {step_class}">
            <div class="step-number {number_class}">{step_num}</div>
            <div>{step_name}</div>
        </div>
        """, unsafe_allow_html=True)

# Helper functions
def calculate_trip_days(start_date, end_date):
    return (end_date - start_date).days + 1

def format_date_range(start_date, end_date):
    return f"{start_date.strftime('%B %d')} to {end_date.strftime('%B %d')}"

# Step 1: Trip Preferences
if st.session_state.current_step == 1:
    st.header("📍 Step 1: Tell Us About Your Trip")
    
    with st.form("trip_preferences"):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("<div class='card-title' style='font-weight:600;'>Your Travel Preferences</div>", unsafe_allow_html=True)

            st.session_state.travel_data['preferences'] = st.text_input(
                "Preferred region(s) in India (e.g., Beaches, Mountains, Cities)",
                value=st.session_state.travel_data.get('preferences', ''),
                placeholder="Where would you like to go?"
            )
            st.session_state.travel_data['interests'] = st.text_area(
                "Your interests/activities (e.g., Sightseeing, Adventure, Food)",
                value=st.session_state.travel_data.get('interests', ''),
                placeholder="What do you enjoy doing?"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("<div class='card-title' style='font-weight:600;'>Trip Dates & Departure</div>", unsafe_allow_html=True)

            today = datetime.today().date()
            max_date = today + timedelta(days=365)

            # Start date picker
            selected_start_date = st.date_input(
                "Start Date",
                value=datetime.strptime(
                    st.session_state.travel_data.get('start_date', today.strftime('%Y-%m-%d')),
                    '%Y-%m-%d'
                ).date(),
                min_value=today,
                max_value=max_date
            )

            # End date picker (completely independent selection)
            selected_end_date = st.date_input(
                "End Date",
                value=datetime.strptime(
                    st.session_state.travel_data.get('end_date', (today + timedelta(days=1)).strftime('%Y-%m-%d')),
                    '%Y-%m-%d'
                ).date(),
                min_value=today,  # Can be same as start date
                max_value=max_date
            )

            # Store the exact dates user selected
            st.session_state.travel_data['start_date'] = selected_start_date.strftime('%Y-%m-%d')
            st.session_state.travel_data['end_date'] = selected_end_date.strftime('%Y-%m-%d')

            st.session_state.travel_data['departure_city'] = st.text_input(
                "Departure City",
                value=st.session_state.travel_data.get('departure_city', 'Mumbai'),
                placeholder="Where are you traveling from?"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("← Back", type="secondary"):
                st.session_state.current_step = 1
                st.rerun()
        with col2:
            submitted = st.form_submit_button("Next: Find Destinations →", type="primary")

        if submitted:
            # Basic validation
            start_date = datetime.strptime(st.session_state.travel_data['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(st.session_state.travel_data['end_date'], '%Y-%m-%d').date()
            
            if end_date < start_date:
                st.error("End date cannot be before start date.")
            elif not st.session_state.travel_data['preferences'] or not st.session_state.travel_data['interests']:
                st.error("Please fill in all required fields.")
            else:
                st.session_state.current_step = 2
                st.rerun()
# Step 2: Destination Selection
elif st.session_state.current_step == 2:
    st.header("🌍 Step 2: Choose Your Destination")
    
    
    # Clear previous destinations if preferences changed
    if 'last_preferences' not in st.session_state or st.session_state.last_preferences != st.session_state.travel_data['preferences']:
        st.session_state.destinations = []
    
    if not st.session_state.destinations:
        with st.spinner("✈️ Finding perfect destinations for you..."):
            try:
                # Get dynamic destinations from agent
                destination_response = destination(
                    preferences=st.session_state.travel_data['preferences'],
                    budget=50000,  # Default budget for initial selection
                    interests=st.session_state.travel_data['interests']
                )
                
                # Parse the bullet point response
                if isinstance(destination_response, str):
                    destinations_list = [line.strip('- *•').strip() for line in destination_response.split('\n') if line.strip()]
                    st.session_state.destinations = destinations_list
                    st.session_state.last_preferences = st.session_state.travel_data['preferences']
                
                if not st.session_state.destinations:
                    st.error("No destinations found matching your criteria. Please adjust your preferences.")
                    st.session_state.current_step = 1
                    st.rerun()
                    
            except Exception as e:
                st.error(f"Error fetching destinations: {str(e)}")
                st.session_state.destinations = []
    
    if st.session_state.destinations:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='font-weight:600; margin-bottom:1rem;'>We found these destinations matching your preferences:</div>
        <div style='margin-bottom: 1.5rem; color: {TEXT_COLOR};'>Based on your interests in <span style='color: {PRIMARY_COLOR}; font-weight: 600;'>{st.session_state.travel_data['interests']}</span> and preference for <span style='color: {PRIMARY_COLOR}; font-weight: 600;'>{st.session_state.travel_data['preferences']}</span> regions</div>
        """, unsafe_allow_html=True)
        
        selected = st.radio(
            "Select your preferred destination:",
            st.session_state.destinations,
            index=st.session_state.travel_data.get('destination_index', 0),
            key="destination_radio"
        )
        
        st.session_state.travel_data['destination'] = selected
        st.session_state.travel_data['destination_index'] = st.session_state.destinations.index(selected)
        st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Preferences", type="secondary"):
                st.session_state.current_step = 1
                st.rerun()
        with col2:
            if st.button("Next: Flight Options →", type="primary"):
                st.session_state.current_step = 3
                st.rerun()

# Step 3: Flight Options
elif st.session_state.current_step == 3:
    st.header("✈️ Step 3: Flight Options")
    
    # Validation checks
    required_fields = ['departure_city', 'destination', 'start_date', 'end_date']
    if not all(field in st.session_state.travel_data for field in required_fields):
        st.error("Missing trip information. Please go back to Step 1.")
        st.stop()
    
    # Convert string dates back to date objects with proper error handling
    try:
        start_date = datetime.strptime(st.session_state.travel_data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(st.session_state.travel_data['end_date'], '%Y-%m-%d').date()
    except (ValueError, KeyError) as e:
        st.error(f"Invalid date format in session data: {str(e)}")
        st.stop()
    
    # Display the actual dates being used
    st.markdown(f"""
    <div class='card info-card'>
        <strong>Trip Dates:</strong> {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize flight results
    if 'flight_result' not in st.session_state:
        st.session_state.flight_result = None
    
    # Flight search - only if we have valid dates
    if st.session_state.flight_result is None:
        with st.spinner("🛫 Searching for flight options..."):
            try:
                # Ensure we're passing the correct dates in YYYY-MM-DD format
                departure_date = start_date.strftime('%Y-%m-%d')
                return_date = end_date.strftime('%Y-%m-%d')
                
                st.write(f"Searching flights from {st.session_state.travel_data['departure_city']} to "
                        f"{st.session_state.travel_data['destination']} on {departure_date} to {return_date}")
                
                flight_result = flight_planner_agent(
                    origin_city=st.session_state.travel_data['departure_city'],
                    destination_city=st.session_state.travel_data['destination'],
                    departure_date=departure_date,
                    return_date=return_date
                )
                st.session_state.flight_result = flight_result
            except Exception as e:
                st.error(f"Flight search failed: {str(e)}")
                st.session_state.flight_result = False
    
    # Display results
    if st.session_state.flight_result and isinstance(st.session_state.flight_result, dict):
        # Process flight data into consistent format
        flight_data = {
            'airline': st.session_state.flight_result.get('airline'),
            'flight_number': st.session_state.flight_result.get('flight_number'),
            'departure_airport': st.session_state.flight_result.get('departure', {}).get('airport'),
            'arrival_airport': st.session_state.flight_result.get('arrival', {}).get('airport'),
            'departure_city': st.session_state.flight_result.get('departure', {}).get('city') or st.session_state.travel_data['departure_city'],
            'arrival_city': st.session_state.flight_result.get('arrival', {}).get('city') or st.session_state.travel_data['destination'],
            'departure_time': st.session_state.flight_result.get('departure', {}).get('time'),
            'arrival_time': st.session_state.flight_result.get('arrival', {}).get('time'),
            'price': st.session_state.flight_result.get('price'),
            'duration': st.session_state.flight_result.get('duration')
        }
        
        # Store in session state
        st.session_state.selected_flight = flight_data
        
        # Display flight info
        st.success("🎉 Flight found! Here are your details:")
        st.markdown(f"""
        - **Airline:** {flight_data['airline']} {flight_data['flight_number']}
        - **Route:** {flight_data['departure_airport']} → {flight_data['arrival_airport']}
        - **Departure:** {flight_data['departure_time']} on {start_date.strftime('%B %d, %Y')}
        - **Arrival:** {flight_data['arrival_time']} on {end_date.strftime('%B %d, %Y')}
        - **Duration:** {flight_data['duration']}
        - **Price:** ₹{flight_data['price']:,}
        """)
    elif st.session_state.flight_result is False:
        st.warning("Could not find flight options for the selected dates.")
    
    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Destinations", type="secondary"):
            st.session_state.current_step -= 1
            st.rerun()
    with col2:
        if st.button("Continue to Budget →", disabled=not st.session_state.get('selected_flight')):
            st.session_state.current_step += 1
            st.rerun()
# Step 4: Budget Calculation
elif st.session_state.current_step == 4:
    st.header("💰 Step 4: Plan Your Budget")
    
    with st.form("budget_form"):
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.selectbox(
            "Accommodation type:",
            ["Budget hostel", "Budget hotel", "3-star hotel", "4-star hotel", "5-star hotel", "Luxury resort"],
            key='accommodation_type',
            index=1
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.form_submit_button("Calculate Budget", type="primary"):
            with st.spinner("Calculating..."):
                try:
                    # Convert string dates back to date objects
                    start_date = datetime.strptime(st.session_state.travel_data['start_date'], '%Y-%m-%d').date()
                    end_date = datetime.strptime(st.session_state.travel_data['end_date'], '%Y-%m-%d').date()
                    
                    flight_cost = st.session_state.get('selected_flight', {}).get('price', 0)
                    
                    # Format dates for the budget agent
                    date_range = f"{start_date.strftime('%B %d')} to {end_date.strftime('%B %d')}"
                    
                    # Call budget calculation with only the expected parameters
                    calculated_budget = calculate_budget(
                        destination=st.session_state.travel_data['destination'],
                        dates=date_range,
                        accommodation_type=st.session_state.accommodation_type,
                        flight_location=st.session_state.travel_data['departure_city'],
                        interests=st.session_state.travel_data['interests'],
                        flight_cost=flight_cost
                    )
                    
                    # Calculate trip duration for display purposes only
                    trip_duration = (end_date - start_date).days + 1
                    
                    # Store results
                    st.session_state.travel_data['calculated_budget'] = calculated_budget
                    st.session_state.budget_result = f"""
                    ### 💵 Your Budget
                    - Total Budget: ₹{calculated_budget:,}
                    - Accommodation: {st.session_state.accommodation_type}
                    - Trip Duration: {trip_duration} days
                    - Includes flights: {'Yes' if flight_cost else 'No'}
                    """
                    
                except Exception as e:
                    st.error(f"Budget calculation failed: {str(e)}")

    if 'budget_result' in st.session_state:
        st.markdown("<div class='card success-card'>", unsafe_allow_html=True)
        st.markdown(st.session_state.budget_result, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Flights", type="secondary"):
            st.session_state.current_step = 3
            st.rerun()
    with col2:
        if st.button("Next: Itinerary →", type="primary"):
            st.session_state.current_step = 5
            st.rerun()

elif st.session_state.current_step == 5:
    st.header("📅 Your Travel Itinerary")
    
    # Get trip data
    budget = st.session_state.travel_data.get('calculated_budget', 50000)
    selected_flight = st.session_state.get('selected_flight', {})
    destination = st.session_state.travel_data['destination']
    interests = st.session_state.travel_data['interests']
    
    # Process dates
    try:
        start_date = datetime.strptime(st.session_state.travel_data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(st.session_state.travel_data['end_date'], '%Y-%m-%d').date()
        duration = (end_date - start_date).days + 1
    except (ValueError, KeyError) as e:
        st.error(f"Date error: {str(e)}")
        st.stop()

    # Display trip summary
    st.markdown(f"""
    ### 🗓️ Trip Summary
    **📍 Destination:** {destination}  
    **📅 Dates:** {start_date.strftime('%b %d')} - {end_date.strftime('%b %d %Y')} ({duration} days)  
    **💰 Budget:** ₹{budget:,}  
    **🎯 Interests:** {interests}
    """)

    # Show flight details if available
    if selected_flight:
        st.markdown(f"""
        ### ✈️ Flight Details
        **Airline:** {selected_flight.get('airline', '')} {selected_flight.get('flight_number', '')}
        **Departure:** {selected_flight.get('departure', {}).get('datetime', '')}  
        **Arrival:** {selected_flight.get('arrival', {}).get('datetime', '')}  
        **Duration:** {selected_flight.get('duration', '')}
        """)

    # Generate itinerary
    if 'itinerary_result' not in st.session_state:
        with st.spinner("Creating your personalized itinerary..."):
            # Prepare flight details structure
            flight_data = None
            if selected_flight:
                flight_data = {
                    "airline": selected_flight.get("airline", ""),
                    "flight_number": selected_flight.get("flight_number", ""),
                    "arrival": {
                        "airport": selected_flight.get("arrival", {}).get("airport", ""),
                        "city": selected_flight.get("arrival", {}).get("city", destination),
                        "time": selected_flight.get("arrival", {}).get("time", "")
                    },
                    "departure": {
                        "airport": selected_flight.get("departure", {}).get("airport", ""),
                        "time": selected_flight.get("departure", {}).get("time", "")
                    },
                    "return_flight": selected_flight.get("return_flight")
                }

            # Generate itinerary
            st.session_state.itinerary_result = generate_itinerary(
                destination=destination,
                dates={
                    'start_date': start_date.strftime('%Y-%m-%d'),
                    'end_date': end_date.strftime('%Y-%m-%d'),
                    'duration': duration,
                    'date_range': f"{start_date.strftime('%b %d')} - {end_date.strftime('%b %d')}"
                },
                budget=budget,
                interests=interests,
                flight_details=flight_data
            )

    # Display itinerary
    if st.session_state.itinerary_result:
        st.markdown(st.session_state.itinerary_result, unsafe_allow_html=True)
        
        # Download button
        st.download_button(
            "📥 Download Itinerary",
            st.session_state.itinerary_result,
            file_name=f"{destination}_itinerary.md",
            mime="text/markdown"
        )

    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back", key="itinerary_back"):
            st.session_state.current_step -= 1
            st.rerun()
    with col2:
        if st.button("Next →", key="itinerary_next"):
            st.session_state.current_step += 1
            st.rerun()

# Step 6: Weather Forecast
elif st.session_state.current_step == 6:
    st.header("☀️ Step 6: Weather Forecast")
    
    # Convert string dates back to date objects first
    try:
        start_date = datetime.strptime(st.session_state.travel_data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(st.session_state.travel_data['end_date'], '%Y-%m-%d').date()
    except (ValueError, KeyError) as e:
        st.error(f"Invalid date format in session data: {str(e)}")
        st.stop()

    if 'weather_result' not in st.session_state:
        with st.spinner("🌤️ Checking weather for your destination..."):
            try:
                # Get the weather forecast using date objects
                weather_result = weather_forecast(
                    city=st.session_state.travel_data['destination'],
                )
                
                # Process the weather result
                if isinstance(weather_result, dict):
                    weather_text = f"### Weather Forecast for {st.session_state.travel_data['destination']}\n\n"
                    for date, forecast in weather_result.items():
                        weather_text += f"**{date}**: {forecast}\n\n"
                    st.session_state.weather_result = weather_text
                else:
                    st.session_state.weather_result = str(weather_result)
                    
            except Exception as e:
                st.error(f"Weather forecast failed: {str(e)}")
                st.session_state.weather_result = "Weather information is currently unavailable."
    
    st.markdown("<div class='card info-card'>", unsafe_allow_html=True)
    st.markdown(f"### {st.session_state.travel_data['destination']} Weather Forecast")
    st.markdown(f"**Travel Dates:** {start_date.strftime('%B %d')} to {end_date.strftime('%B %d')}")
    
    # Display the weather information
    if st.session_state.weather_result:
        st.markdown(st.session_state.weather_result, unsafe_allow_html=True)
    else:
        st.warning("Could not retrieve weather information for this destination.")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Completion card
    st.markdown("<div class='card success-card'>", unsafe_allow_html=True)
    st.markdown("### 🎉 Your Travel Plan is Complete!")
    st.markdown(f"""
    You're all set for your trip to **{st.session_state.travel_data['destination']}** from **{start_date.strftime('%B %d')} to {end_date.strftime('%B %d')}**!
    
    Here's what we've prepared for you:
    - Selected destination based on your preferences
    - Budget estimation for your trip
    - Flight options from {st.session_state.travel_data['departure_city']}
    - Detailed day-by-day itinerary
    - Weather forecast for your travel dates
    
    Have a wonderful trip! ✈️🌴
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Itinerary", type="secondary"):
            st.session_state.current_step = 5
            st.rerun()
    with col2:
        if st.button("✨ Start New Trip", type="primary"):
            st.session_state.current_step = 1
            st.session_state.travel_data = {}
            st.session_state.destinations = []
            st.session_state.destination_details = {}
            st.session_state.clear()
            st.rerun()

# Footer with subtle background
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: {TEXT_COLOR}; font-size: small; padding: 1rem; background-color: rgba(229, 231, 235, 0.3); border-radius: 8px;">
    <p style="font-weight: 600; color: {PRIMARY_COLOR};">Travel Buddy - Your Smart Travel Assistant</p>
    <p style="color: {TEXT_COLOR};">Note: All prices and availability are estimates. Please verify with service providers.</p>
</div>
""", unsafe_allow_html=True)