import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
os.environ['GROQ_API_KEY'] = st.secrets["GROQ_API_KEY"]

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(model_name='Gemma2-9b-It')

def generate_itinerary(destination, dates, budget, interests, flight_details=None):
    """
    Generate a detailed travel itinerary with flight information, daily activities, and budget breakdown
    
    Args:
        destination (str): Travel destination city
        dates (dict): Contains start_date, end_date, duration
        budget (int): Total trip budget in INR
        interests (str): Traveler's interests
        flight_details (dict): Flight arrival/departure details
    
    Returns:
        str: Formatted markdown itinerary
    """
    try:
        # Validate inputs
        if not destination or not isinstance(destination, str):
            return "❌ Invalid destination provided"
            
        if not dates or 'duration' not in dates:
            return "❌ Invalid dates provided"
            
        try:
            budget = max(int(budget), 20000)  # Ensure minimum budget
        except (ValueError, TypeError):
            budget = 50000  # Default budget if invalid
            
        duration = int(dates.get('duration', 2))
        if duration < 1:
            duration = 2  # Minimum duration
            
        daily_budget = int(budget / duration)

        # Build arrival section safely
        arrival_section = build_arrival_section(destination, flight_details, daily_budget)
        
        # Generate activity days safely
        activity_days = build_activity_days(destination, duration, interests, daily_budget)
        
        # Add departure day if return flight exists
        if flight_details and isinstance(flight_details, dict) and flight_details.get('return_flight'):
            activity_days += build_departure_section(destination, duration, flight_details, daily_budget)

        # Prepare flight info string safely
        flight_info = ""
        if flight_details and isinstance(flight_details, dict):
            flight_info = f"""
Flight Details:
- Airline: {flight_details.get('airline', 'Unknown')}
- Flight Number: {flight_details.get('flight_number', '')}
- Departure: {flight_details.get('departure', {}).get('datetime', 'Not specified')}
- Arrival: {flight_details.get('arrival', {}).get('datetime', 'Not specified')}
- Duration: {flight_details.get('duration', 'Not specified')}
"""
            if flight_details.get('return_flight'):
                flight_info += f"""
Return Flight:
- Airline: {flight_details['return_flight'].get('airline', 'Unknown')}
- Flight Number: {flight_details['return_flight'].get('flight_number', '')}
- Departure: {flight_details['return_flight'].get('departure', {}).get('datetime', 'Not specified')}
- Arrival: {flight_details['return_flight'].get('arrival', {}).get('datetime', 'Not specified')}
- Duration: {flight_details['return_flight'].get('duration', 'Not specified')}
"""

        # Generate the full itinerary
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You're a professional travel designer. Create detailed itineraries with:
             - Creative day titles with emojis
             - Well-timed morning/afternoon/evening activities
             - Local restaurant and attraction recommendations
             - Transportation notes
             - Budget estimates
             - Insider tips"""),
            ("human", """Create a {duration}-day itinerary for {destination} with ₹{budget:,} budget.
            
**Traveler Interests:** {interests}
**Flight Information:** {flight_info}

**Output Requirements:**
1. Each day gets a creative title (emoji + catchy phrase)
2. Group activities into Morning/Afternoon/Evening
3. Include specific timings, venue names, and costs
4. Add local tips and transportation notes
5. Use consistent markdown formatting

**Itinerary Framework:**
{itinerary_framework}""")
        ])

        # Generate and format the output
        chain = prompt | llm
        result = chain.invoke({
            "destination": destination,
            "duration": duration,
            "budget": budget,
            "interests": interests,
            "flight_info": flight_info,
            "itinerary_framework": arrival_section + activity_days
        })
        
        # Safely get content from result
        content = result.content if hasattr(result, 'content') else str(result)
        
        return format_final_itinerary(destination, duration, budget, interests, content)

    except Exception as e:
        return f"❌ Itinerary generation failed: {str(e)}"

def build_arrival_section(destination, flight_details, daily_budget):
    """Build the arrival day section of the itinerary safely"""
    try:
        if flight_details and isinstance(flight_details, dict):
            arrival = flight_details.get('arrival', {})
            return f"""
### ✈️ **Day 1: Arrival in {destination}**  
**🏨 *Settling In***  

**Flight Details:**  
🛬 {arrival.get('time', 'Afternoon')} - {flight_details.get('airline', 'Unknown')} {flight_details.get('flight_number', '')}  
📍 {arrival.get('airport', 'Airport')}  

**Upon Arrival:**  
⏰ 1-2 hours - Baggage claim & transfers  
🚕 Transfer to accommodation  
🏨 Check-in and freshen up  

**Evening:**  
🌆 Explore nearby area  
🍽️ Dinner at local restaurant  
💤 Rest for next day  

**💰 Budget:** ₹{daily_budget:,}  
"""
        return f"""
### 🏨 **Day 1: Welcome to {destination}**  
**🌟 *First Impressions***  

**Afternoon/Evening:**  
🏨 Hotel check-in  
🚶‍♂️ Neighborhood walk  
🍜 Local cuisine dinner  

**💰 Budget:** ₹{daily_budget:,}  
"""
    except Exception:
        return f"""
### 🏨 **Day 1: Welcome to {destination}**  
**🌟 *First Impressions***  

**Afternoon/Evening:**  
🏨 Hotel check-in  
🚶‍♂️ Neighborhood walk  
🍜 Local cuisine dinner  

**💰 Budget:** ₹{daily_budget:,}  
"""

def build_activity_days(destination, duration, interests, daily_budget):
    """Build the main activity days section safely"""
    try:
        activity_days = ""
        for day in range(2, duration + 1):
            activity_days += f"""
### 🌟 **Day {day}: Exploring {destination}**  
**🌅 Morning**  
☕ 8:00 AM - Breakfast  
🏛️ 9:30 AM - {interests}-focused activity  
⏰ 12:00 PM - Lunch  

**🌞 Afternoon**  
🚤 2:00 PM - Local experience  
🏞️ 4:30 PM - Landmark visit  

**🌃 Evening**  
🌇 6:00 PM - Sunset viewing  
🍸 8:00 PM - Dinner  

**💰 Budget:** ₹{daily_budget:,}  
"""
        return activity_days
    except Exception:
        return ""

def build_departure_section(destination, duration, flight_details, daily_budget):
    """Build the departure day section safely"""
    try:
        if not flight_details or not isinstance(flight_details, dict):
            return ""
            
        return_flight = flight_details.get('return_flight', {})
        if not return_flight:
            return ""
            
        departure = return_flight.get('departure', {})
        return f"""
### ✈️ **Day {duration}: Departure**  
**🛫 *Final Day***  

**Morning:**  
🧳 Check-out by 11 AM  
🚕 Airport transfer  
☕ Airport breakfast  

**Flight:**  
🛫 {departure.get('time', 'Not specified')} - {return_flight.get('airline', 'Unknown')} {return_flight.get('flight_number', '')}  
📍 {departure.get('airport', 'Airport')}  

**💰 Budget:** ₹{int(daily_budget*0.5):,}  
"""
    except Exception:
        return ""

def format_final_itinerary(destination, duration, budget, interests, content):
    """Format the final itinerary output safely"""
    try:
        return f"""
# ✈️ {destination} Itinerary ({duration} Days)
**💰 Budget:** ₹{budget:,} | **🌍 Interests:** {interests}  

---

{content}

---
## 📌 Travel Tips:
💡 *Local Insight:* Ask locals for hidden gems!  
⚠️ *Note:* Check weather forecasts before outdoor activities  
📱 *Helpful Apps:* Google Maps, local transit apps  

Enjoy your trip! 🎉
"""
    except Exception:
        return content  # Return raw content if formatting fails