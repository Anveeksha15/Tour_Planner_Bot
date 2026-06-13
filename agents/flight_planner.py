import random
import streamlit as st
from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# AIRPORT DATABASE (IATA codes)
# ─────────────────────────────────────────────
AIRPORT_DB = {
    # India
    "delhi": "DEL", "new delhi": "DEL", "ndls": "DEL",
    "mumbai": "BOM", "bombay": "BOM",
    "bangalore": "BLR", "bengaluru": "BLR",
    "chennai": "MAA", "madras": "MAA",
    "kolkata": "CCU", "calcutta": "CCU",
    "hyderabad": "HYD",
    "pune": "PNQ",
    "ahmedabad": "AMD",
    "jaipur": "JAI",
    "goa": "GOI", "panaji": "GOI",
    "kochi": "COK", "cochin": "COK",
    "lucknow": "LKO",
    "chandigarh": "IXC",
    "amritsar": "ATQ",
    "nagpur": "NAG",
    "bhopal": "BHO",
    "indore": "IDR",
    "varanasi": "VNS",
    "patna": "PAT",
    "ranchi": "IXR",
    "bhubaneswar": "BBI",
    "visakhapatnam": "VTZ", "vizag": "VTZ",
    "coimbatore": "CJB",
    "madurai": "IXM",
    "thiruvananthapuram": "TRV", "trivandrum": "TRV",
    "srinagar": "SXR",
    "jammu": "IXJ",
    "dehradun": "DED",
    "leh": "IXL",
    "udaipur": "UDR",
    "jodhpur": "JDH",
    "raipur": "RPR",
    "mangalore": "IXE",
    "hubli": "HBX",
    "aurangabad": "IXU",
    # International
    "dubai": "DXB",
    "abu dhabi": "AUH",
    "singapore": "SIN",
    "bangkok": "BKK",
    "london": "LHR",
    "new york": "JFK",
    "paris": "CDG",
    "tokyo": "NRT",
    "sydney": "SYD",
    "toronto": "YYZ",
    "frankfurt": "FRA",
    "amsterdam": "AMS",
    "kuala lumpur": "KUL",
    "hong kong": "HKG",
    "doha": "DOH",
    "muscat": "MCT",
    "colombo": "CMB",
    "kathmandu": "KTM",
    "dhaka": "DAC",
    "islamabad": "ISB",
    "karachi": "KHI",
    "nairobi": "NBO",
    "johannesburg": "JNB",
    "melbourne": "MEL",
}

# ─────────────────────────────────────────────
# NEARBY AIRPORT MAPPING
# Maps city/region names (without direct airports) to the
# nearest airport city name that IS in AIRPORT_DB.
# ─────────────────────────────────────────────
NEARBY_AIRPORT_MAP = {
    # Rajasthan
    "pushkar": ("ajmer", "Jaipur", "JAI", "~145 km via Ajmer"),
    "ajmer": ("jaipur", "Jaipur", "JAI", "~132 km"),
    "mount abu": ("udaipur", "Udaipur", "UDR", "~163 km"),
    "ranthambore": ("jaipur", "Jaipur", "JAI", "~180 km"),
    "bikaner": ("jaipur", "Jaipur", "JAI", "~330 km"),

    # Himachal Pradesh / Uttarakhand
    "manali": ("kullu", "Kullu-Manali (KUU) or Chandigarh", "IXC", "~310 km via Chandigarh"),
    "shimla": ("chandigarh", "Chandigarh", "IXC", "~120 km"),
    "dharamshala": ("chandigarh", "Chandigarh", "IXC", "~240 km"),
    "mcleod ganj": ("chandigarh", "Chandigarh", "IXC", "~245 km"),
    "kasol": ("chandigarh", "Chandigarh", "IXC", "~270 km"),
    "mussoorie": ("dehradun", "Dehradun", "DED", "~35 km"),
    "rishikesh": ("dehradun", "Dehradun", "DED", "~45 km"),
    "haridwar": ("dehradun", "Dehradun", "DED", "~55 km"),
    "nainital": ("pantnagar", "Pantnagar (PGH) or Dehradun", "DED", "~65 km via Pantnagar"),
    "auli": ("dehradun", "Dehradun", "DED", "~298 km"),
    "kedarnath": ("dehradun", "Dehradun", "DED", "~235 km"),
    "badrinath": ("dehradun", "Dehradun", "DED", "~317 km"),
    "spiti valley": ("chandigarh", "Chandigarh", "IXC", "~450 km"),
    "chopta": ("dehradun", "Dehradun", "DED", "~225 km"),
    "lansdowne": ("dehradun", "Dehradun", "DED", "~145 km"),

    # Kerala
    "munnar": ("kochi", "Kochi", "COK", "~130 km"),
    "alleppey": ("kochi", "Kochi", "COK", "~85 km"),
    "alappuzha": ("kochi", "Kochi", "COK", "~85 km"),
    "varkala": ("thiruvananthapuram", "Thiruvananthapuram", "TRV", "~50 km"),
    "thekkady": ("kochi", "Kochi", "COK", "~185 km"),
    "wayanad": ("kochi", "Kochi", "COK", "~295 km"),
    "kovalam": ("thiruvananthapuram", "Thiruvananthapuram", "TRV", "~16 km"),
    "kumarakom": ("kochi", "Kochi", "COK", "~75 km"),

    # Goa & surroundings
    "north goa": ("goa", "Goa", "GOI", "~30 km"),
    "south goa": ("goa", "Goa", "GOI", "~45 km"),
    "calangute": ("goa", "Goa", "GOI", "~40 km"),
    "vagator": ("goa", "Goa", "GOI", "~42 km"),
    "palolem": ("goa", "Goa", "GOI", "~68 km"),
    "hampi": ("hubli", "Hubli", "HBX", "~160 km"),

    # Maharashtra
    "lonavala": ("pune", "Pune", "PNQ", "~65 km"),
    "mahabaleshwar": ("pune", "Pune", "PNQ", "~120 km"),
    "nashik": ("mumbai", "Mumbai", "BOM", "~165 km"),
    "shirdi": ("aurangabad", "Aurangabad", "IXU", "~85 km"),
    "kolhapur": ("pune", "Pune", "PNQ", "~228 km"),
    "alibaug": ("mumbai", "Mumbai", "BOM", "~95 km"),

    # Tamil Nadu
    "ooty": ("coimbatore", "Coimbatore", "CJB", "~86 km"),
    "kodaikanal": ("madurai", "Madurai", "IXM", "~120 km"),
    "mahabalipuram": ("chennai", "Chennai", "MAA", "~60 km"),
    "pondicherry": ("chennai", "Chennai", "MAA", "~160 km"),
    "puducherry": ("chennai", "Chennai", "MAA", "~160 km"),
    "rameshwaram": ("madurai", "Madurai", "IXM", "~174 km"),
    "kanyakumari": ("thiruvananthapuram", "Thiruvananthapuram", "TRV", "~90 km"),
    "vellore": ("chennai", "Chennai", "MAA", "~135 km"),

    # Karnataka
    "coorg": ("mangalore", "Mangalore", "IXE", "~160 km"),
    "chikmagalur": ("mangalore", "Mangalore", "IXE", "~150 km"),
    "mysore": ("bangalore", "Bangalore", "BLR", "~145 km"),
    "mysuru": ("bangalore", "Bangalore", "BLR", "~145 km"),
    "badami": ("hubli", "Hubli", "HBX", "~120 km"),

    # Andhra Pradesh / Telangana
    "araku valley": ("visakhapatnam", "Visakhapatnam", "VTZ", "~115 km"),
    "tirupati": ("chennai", "Chennai", "MAA", "~140 km"),

    # Odisha
    "puri": ("bhubaneswar", "Bhubaneswar", "BBI", "~65 km"),
    "konark": ("bhubaneswar", "Bhubaneswar", "BBI", "~65 km"),
    "chilika lake": ("bhubaneswar", "Bhubaneswar", "BBI", "~100 km"),

    # Gujarat
    "kutch": ("ahmedabad", "Ahmedabad", "AMD", "~330 km"),
    "rann of kutch": ("ahmedabad", "Ahmedabad", "AMD", "~330 km"),
    "dwarka": ("ahmedabad", "Ahmedabad", "AMD", "~450 km"),
    "somnath": ("ahmedabad", "Ahmedabad", "AMD", "~380 km"),
    "gir": ("ahmedabad", "Ahmedabad", "AMD", "~360 km"),
    "saputara": ("surat", "Surat (STV) or Ahmedabad", "AMD", "~165 km via Surat"),

    # Jammu & Kashmir / Ladakh
    "gulmarg": ("srinagar", "Srinagar", "SXR", "~56 km"),
    "pahalgam": ("srinagar", "Srinagar", "SXR", "~95 km"),
    "sonamarg": ("srinagar", "Srinagar", "SXR", "~80 km"),
    "pangong lake": ("leh", "Leh", "IXL", "~160 km"),
    "nubra valley": ("leh", "Leh", "IXL", "~120 km"),
    "kargil": ("leh", "Leh", "IXL", "~230 km"),

    # Madhya Pradesh
    "khajuraho": ("varanasi", "Varanasi (VNS) or Khajuraho (HJR)", "VNS", "~280 km via Varanasi"),
    "orchha": ("bhopal", "Bhopal", "BHO", "~380 km"),
    "pachmarhi": ("bhopal", "Bhopal", "BHO", "~195 km"),
    "kanha": ("nagpur", "Nagpur", "NAG", "~285 km"),
    "bandhavgarh": ("jabalpur", "Jabalpur (JLR) or Varanasi", "VNS", "~237 km via Jabalpur"),
    "pench": ("nagpur", "Nagpur", "NAG", "~90 km"),

    # Northeast India
    "kaziranga": ("guwahati", "Guwahati (GAU)", "GAU", "~190 km"),
    "shillong": ("guwahati", "Guwahati (GAU)", "GAU", "~100 km"),
    "cherrapunji": ("guwahati", "Guwahati (GAU)", "GAU", "~150 km"),
    "gangtok": ("bagdogra", "Bagdogra (IXB)", "IXB", "~125 km"),
    "darjeeling": ("bagdogra", "Bagdogra (IXB)", "IXB", "~70 km"),
    "sikkim": ("bagdogra", "Bagdogra (IXB)", "IXB", "~110 km"),

    # West Bengal
    "sundarbans": ("kolkata", "Kolkata", "CCU", "~100 km"),
    "digha": ("kolkata", "Kolkata", "CCU", "~185 km"),

    # Uttar Pradesh / Bihar
    "agra": ("delhi", "Delhi", "DEL", "~230 km"),
    "mathura": ("delhi", "Delhi", "DEL", "~160 km"),
    "vrindavan": ("delhi", "Delhi", "DEL", "~155 km"),
    "allahabad": ("varanasi", "Varanasi", "VNS", "~140 km"),
    "prayagraj": ("varanasi", "Varanasi", "VNS", "~140 km"),
    "ayodhya": ("lucknow", "Lucknow", "LKO", "~135 km"),
    "gorakhpur": ("varanasi", "Varanasi", "VNS", "~275 km"),
    "bodh gaya": ("patna", "Patna", "PAT", "~120 km"),
    "nalanda": ("patna", "Patna", "PAT", "~90 km"),
}

# Airlines with realistic codes and names
AIRLINES = [
    {"code": "AI", "name": "Air India"},
    {"code": "6E", "name": "IndiGo"},
    {"code": "SG", "name": "SpiceJet"},
    {"code": "UK", "name": "Vistara"},
    {"code": "G8", "name": "Go First"},
    {"code": "IX", "name": "Air Asia India"},
    {"code": "QP", "name": "Akasa Air"},
]

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def get_iata_code(city_name: str) -> str | None:
    """Look up IATA code from city name."""
    if not city_name:
        return None
    key = city_name.strip().lower()
    if key in AIRPORT_DB:
        return AIRPORT_DB[key]
    for city, code in AIRPORT_DB.items():
        if city in key or key in city:
            return code
    return None


def get_nearby_airport_info(city_name: str) -> dict | None:
    """
    For cities without a direct airport, return info about the nearest airport.
    Returns dict with keys: iata_code, display_name, distance_note
    or None if not found in NEARBY_AIRPORT_MAP.
    """
    key = city_name.strip().lower()
    if key in NEARBY_AIRPORT_MAP:
        _, display_name, iata_code, distance_note = NEARBY_AIRPORT_MAP[key]
        return {
            "iata_code": iata_code,
            "display_name": display_name,
            "distance_note": distance_note,
        }
    # Partial match
    for place, info in NEARBY_AIRPORT_MAP.items():
        if place in key or key in place:
            _, display_name, iata_code, distance_note = info
            return {
                "iata_code": iata_code,
                "display_name": display_name,
                "distance_note": distance_note,
            }
    return None


def resolve_airport(city_name: str) -> tuple[str | None, str | None, bool]:
    """
    Try to resolve a city to an airport code.
    Returns (iata_code, notice_message, is_nearby).
    - is_nearby=True means we used a nearby airport, not a direct one.
    """
    direct = get_iata_code(city_name)
    if direct:
        return direct, None, False
    nearby = get_nearby_airport_info(city_name)
    if nearby:
        msg = (
            f"ℹ️ **{city_name.title()}** doesn't have a direct airport. "
            f"Showing flights to/from **{nearby['display_name']}** ({nearby['iata_code']}) — "
            f"{nearby['distance_note']}."
        )
        return nearby["iata_code"], msg, True
    return None, None, False


def get_flexible_dates(departure_date: str, return_date: str, window: int = 2) -> list[tuple[str, str]]:
    """
    Generate a list of (dep_date, ret_date) tuples within ±window days of the originals.
    Original dates are always first in the list.
    """
    dep_dt = datetime.strptime(departure_date, "%Y-%m-%d").date()
    ret_dt = datetime.strptime(return_date, "%Y-%m-%d").date()
    today = datetime.now().date()
    combos = []
    for dep_delta in range(-window, window + 1):
        new_dep = dep_dt + timedelta(days=dep_delta)
        if new_dep < today:
            continue
        for ret_delta in range(-window, window + 1):
            new_ret = ret_dt + timedelta(days=ret_delta)
            if new_ret <= new_dep:
                continue
            combos.append((new_dep.strftime("%Y-%m-%d"), new_ret.strftime("%Y-%m-%d")))
    # Sort: original first, then by proximity
    combos.sort(key=lambda c: (abs((datetime.strptime(c[0], "%Y-%m-%d").date() - dep_dt).days) +
                                abs((datetime.strptime(c[1], "%Y-%m-%d").date() - ret_dt).days)))
    return combos


def parse_duration(hours: float) -> str:
    h = int(hours)
    m = int((hours - h) * 60)
    return f"{h}h {m:02d}m" if m else f"{h}h"


def random_time(base_date: str, hour_min: int = 4, hour_max: int = 23) -> datetime:
    date = datetime.strptime(base_date, "%Y-%m-%d")
    hour = random.randint(hour_min, hour_max)
    minute = random.choice([0, 10, 15, 20, 25, 30, 40, 45, 50, 55])
    return date.replace(hour=hour, minute=minute)


def generate_flight_number(airline_code: str) -> str:
    return f"{airline_code}{random.randint(100, 999)}"


def base_price(origin: str, dest: str, adults: int) -> int:
    indian_codes = {v for k, v in AIRPORT_DB.items() if k in [
        "delhi","mumbai","bangalore","chennai","kolkata","hyderabad","pune",
        "ahmedabad","jaipur","goa","kochi","lucknow","chandigarh","amritsar",
        "nagpur","bhopal","indore","varanasi","patna","ranchi","bhubaneswar",
        "visakhapatnam","vizag","coimbatore","madurai","thiruvananthapuram",
        "trivandrum","srinagar","jammu","dehradun","leh","udaipur","jodhpur",
        "raipur","mangalore","hubli","aurangabad","bengaluru","new delhi",
        "bombay","calcutta","madras","panaji","cochin"
    ]}
    is_domestic = (origin in indian_codes and dest in indian_codes)
    per_person = random.randint(3000, 12000) if is_domestic else random.randint(25000, 90000)
    return per_person * adults


# ─────────────────────────────────────────────
# MOCK FLIGHT GENERATOR
# ─────────────────────────────────────────────

def generate_mock_flights(
    origin_code: str,
    dest_code: str,
    departure_date: str,
    return_date: str,
    adults: int,
    count: int = 5
) -> list[dict]:
    offers = []
    used_airlines = random.sample(AIRLINES, min(count, len(AIRLINES)))

    for airline in used_airlines:
        dep_time = random_time(departure_date)
        duration_hrs = round(random.uniform(1.0, 4.5), 2)
        arr_time = dep_time + timedelta(hours=duration_hrs)
        stops_out = random.choices([0, 1], weights=[70, 30])[0]

        ret_dep_time = random_time(return_date)
        ret_duration_hrs = round(random.uniform(1.0, 4.5), 2)
        ret_arr_time = ret_dep_time + timedelta(hours=ret_duration_hrs)
        stops_ret = random.choices([0, 1], weights=[70, 30])[0]

        price = base_price(origin_code, dest_code, adults)
        price = int(price * random.uniform(0.85, 1.25))

        offers.append({
            "airline_code": airline["code"],
            "airline_name": airline["name"],
            "flight_number": generate_flight_number(airline["code"]),
            "price": price,
            "outbound": {
                "origin": origin_code,
                "destination": dest_code,
                "departure_time": dep_time,
                "arrival_time": arr_time,
                "duration": parse_duration(duration_hrs),
                "stops": stops_out,
            },
            "return": {
                "origin": dest_code,
                "destination": origin_code,
                "departure_time": ret_dep_time,
                "arrival_time": ret_arr_time,
                "duration": parse_duration(ret_duration_hrs),
                "stops": stops_ret,
            },
        })

    offers.sort(key=lambda x: x["price"])
    return offers


# ─────────────────────────────────────────────
# MAIN AGENT FUNCTION
# ─────────────────────────────────────────────

def flight_planner_agent(
    origin_city: str,
    destination_city: str,
    departure_date: str,
    return_date: str,
    adults: int = 1
):
    # ── 1. Validate inputs ──
    if not all([origin_city, destination_city, departure_date, return_date]):
        st.error("❌ Please fill in all search fields.")
        return False

    try:
        dep_dt = datetime.strptime(departure_date, "%Y-%m-%d").date()
        ret_dt = datetime.strptime(return_date, "%Y-%m-%d").date()
    except ValueError:
        st.error("❌ Invalid date format. Use YYYY-MM-DD.")
        return False

    if dep_dt < datetime.now().date():
        st.error("❌ Departure date cannot be in the past.")
        return False
    if dep_dt >= ret_dt:
        st.error("❌ Return date must be after departure date.")
        return False
    if not isinstance(adults, int) or not (1 <= adults <= 9):
        st.error("❌ Number of adults must be between 1 and 9.")
        return False

    # ── 2. Resolve IATA codes (with nearby fallback) ──
    origin_code, origin_notice, origin_is_nearby = resolve_airport(origin_city)
    dest_code, dest_notice, dest_is_nearby = resolve_airport(destination_city)

    if not origin_code:
        st.error(f"❌ Could not find an airport for: **{origin_city}**. Try entering the nearest major city.")
        return False
    if not dest_code:
        st.error(f"❌ Could not find an airport for: **{destination_city}**. Try entering the nearest major city.")
        return False
    if origin_code == dest_code:
        st.error("❌ Origin and destination resolve to the same airport. Please check your inputs.")
        return False

    # Show nearby airport notices
    if origin_notice:
        st.info(origin_notice)
    if dest_notice:
        st.info(dest_notice)

    st.info(f"🛫 **{origin_city.title()}** ({origin_code})  →  **{destination_city.title()}** ({dest_code})")

    # ── 3. Try exact dates first, then flexible dates ──
    date_combos = get_flexible_dates(departure_date, return_date, window=2)
    best_dep_date = departure_date
    best_ret_date = return_date
    offers = []
    used_flexible = False
    flexible_dep_date = None
    flexible_ret_date = None

    with st.spinner("🔍 Searching for available flights..."):
        for dep_d, ret_d in date_combos:
            seed = hash((origin_code, dest_code, dep_d, ret_d, adults)) % (2**32)
            random.seed(seed)
            candidate_offers = generate_mock_flights(origin_code, dest_code, dep_d, ret_d, adults)
            if candidate_offers:
                offers = candidate_offers
                best_dep_date = dep_d
                best_ret_date = ret_d
                if dep_d != departure_date or ret_d != return_date:
                    used_flexible = True
                    flexible_dep_date = dep_d
                    flexible_ret_date = ret_d
                break  # Found flights — stop searching

    if not offers:
        st.warning("⚠️ No flights found even with flexible dates. Try a different route or date range.")
        return None

    # ── 4. Notify if flexible dates were used ──
    if used_flexible:
        orig_dep_fmt = datetime.strptime(departure_date, "%Y-%m-%d").strftime("%d %b %Y")
        orig_ret_fmt = datetime.strptime(return_date, "%Y-%m-%d").strftime("%d %b %Y")
        flex_dep_fmt = datetime.strptime(flexible_dep_date, "%Y-%m-%d").strftime("%d %b %Y")
        flex_ret_fmt = datetime.strptime(flexible_ret_date, "%Y-%m-%d").strftime("%d %b %Y")
        st.warning(
            f"⚠️ No flights found for your exact dates (**{orig_dep_fmt}** → **{orig_ret_fmt}**). "
            f"Showing the closest available flights: **{flex_dep_fmt}** → **{flex_ret_fmt}**."
        )

    # ── 5. Also show alternative date options in an expander ──
    if used_flexible or dest_is_nearby or origin_is_nearby:
        with st.expander("🗓️ See other available date combinations nearby"):
            alt_combos = [
                (d, r) for (d, r) in date_combos
                if not (d == best_dep_date and r == best_ret_date)
            ][:6]  # Show at most 6 alternatives
            if alt_combos:
                for d, r in alt_combos:
                    d_fmt = datetime.strptime(d, "%Y-%m-%d").strftime("%d %b %Y")
                    r_fmt = datetime.strptime(r, "%Y-%m-%d").strftime("%d %b %Y")
                    seed = hash((origin_code, dest_code, d, r, adults)) % (2**32)
                    random.seed(seed)
                    alt_offers = generate_mock_flights(origin_code, dest_code, d, r, adults, count=1)
                    if alt_offers:
                        price_hint = f"₹{alt_offers[0]['price']:,}+"
                        st.markdown(f"- **{d_fmt}** → **{r_fmt}** — from {price_hint}")
            else:
                st.write("No nearby alternatives found.")

    st.success(f"✅ Found **{len(offers)} flight options** — sorted by price")

    # ── 6. Init session state ──
    if "selected_flight" not in st.session_state:
        st.session_state.selected_flight = None
    if "travel_data" not in st.session_state:
        st.session_state.travel_data = {}

    # ── 7. Display flights ──
    for i, offer in enumerate(offers, 1):
        out = offer["outbound"]
        ret = offer["return"]

        with st.container(border=True):
            col_airline, col_price = st.columns([3, 1])
            with col_airline:
                st.markdown(f"### ✈️ {offer['airline_name']}  `{offer['flight_number']}`")
            with col_price:
                st.markdown(f"### ₹{offer['price']:,}")
                st.caption(f"for {adults} passenger{'s' if adults > 1 else ''}")

            # Outbound
            st.markdown(f"**🛫 Outbound — {out['departure_time'].strftime('%a, %d %b %Y')}**")
            if dest_is_nearby:
                st.caption(f"🚌 You'll need to travel from {dest_code} airport to {destination_city.title()}")
            c1, c2, c3 = st.columns([2, 2, 2])
            with c1:
                st.metric("From", origin_code)
                st.caption(out["departure_time"].strftime("%H:%M"))
            with c2:
                st.metric("Duration", out["duration"])
                st.caption("Non-stop" if out["stops"] == 0 else f"{out['stops']} stop")
            with c3:
                st.metric("To", dest_code)
                st.caption(out["arrival_time"].strftime("%H:%M"))

            st.divider()

            # Return
            st.markdown(f"**🛬 Return — {ret['departure_time'].strftime('%a, %d %b %Y')}**")
            c1, c2, c3 = st.columns([2, 2, 2])
            with c1:
                st.metric("From", dest_code)
                st.caption(ret["departure_time"].strftime("%H:%M"))
            with c2:
                st.metric("Duration", ret["duration"])
                st.caption("Non-stop" if ret["stops"] == 0 else f"{ret['stops']} stop")
            with c3:
                st.metric("To", origin_code)
                st.caption(ret["arrival_time"].strftime("%H:%M"))

            if st.button(f"Select This Flight — ₹{offer['price']:,}", key=f"flight_{i}"):
                flight_data = {
                    "number": i,
                    "price": offer["price"],
                    "airline": offer["airline_name"],
                    "airline_code": offer["airline_code"],
                    "flight_number": offer["flight_number"],
                    "nearby_airport_used": dest_is_nearby,
                    "nearby_airport_info": dest_notice,
                    "departure": {
                        "airport": origin_code,
                        "city": origin_city.title(),
                        "time": out["departure_time"].strftime("%H:%M"),
                        "date": out["departure_time"].strftime("%Y-%m-%d"),
                        "datetime": out["departure_time"].strftime("%a, %d %b %H:%M"),
                    },
                    "arrival": {
                        "airport": dest_code,
                        "city": destination_city.title(),
                        "time": out["arrival_time"].strftime("%H:%M"),
                        "date": out["arrival_time"].strftime("%Y-%m-%d"),
                        "datetime": out["arrival_time"].strftime("%a, %d %b %H:%M"),
                    },
                    "duration": out["duration"],
                    "stops": out["stops"],
                    "return_flight": {
                        "departure": {
                            "airport": dest_code,
                            "city": destination_city.title(),
                            "time": ret["departure_time"].strftime("%H:%M"),
                            "date": ret["departure_time"].strftime("%Y-%m-%d"),
                            "datetime": ret["departure_time"].strftime("%a, %d %b %H:%M"),
                        },
                        "arrival": {
                            "airport": origin_code,
                            "city": origin_city.title(),
                            "time": ret["arrival_time"].strftime("%H:%M"),
                            "date": ret["arrival_time"].strftime("%Y-%m-%d"),
                            "datetime": ret["arrival_time"].strftime("%a, %d %b %H:%M"),
                        },
                        "duration": ret["duration"],
                        "stops": ret["stops"],
                    },
                }
                st.session_state.selected_flight = flight_data
                st.session_state.travel_data["flight_cost"] = offer["price"]
                st.rerun()

    if st.session_state.get("selected_flight"):
        sf = st.session_state.selected_flight
        st.success(f"✅ Flight selected: **{sf['airline']}** — ₹{sf['price']:,}")
        if sf.get("nearby_airport_used") and sf.get("nearby_airport_info"):
            st.info(sf["nearby_airport_info"])
        return sf

    return None