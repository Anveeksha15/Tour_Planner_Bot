# Travel Buddy - Smart Travel Planning Assistant  

## Overview   

Travel Buddy is an AI-powered travel planning assistant that helps users plan their perfect trip within India. The application guides users through a step-by-step process, from selecting destinations to generating detailed itineraries, using simulated flight data and current weather conditions.  

Powered by **Groq-hosted `openai/gpt-oss-20b`** (destination, itinerary, and weather summarization) and **`llama-3.1-8b-instant`** (budget estimation) for AI-driven recommendations, a **built-in flight simulator** for realistic Indian flight options, and the **OpenWeather API** for current weather conditions, Travel Buddy ensures a seamless and data-driven travel planning experience — with no flight API key required.  

## Features  

### 1. **Trip Planning Workflow**  
- Multi-step process with progress tracking  
- Interactive forms for preferences and dates  
- Visual step indicators in sidebar 

### 2. **Smart Destination Recommendations**  
- AI-powered destination suggestions based on:  
  - Preferred regions (beaches, mountains, cities)  
  - Travel interests (sightseeing, adventure, food)  
  - Budget considerations  
- Uses **Groq's `openai/gpt-oss-20b`** for personalized recommendations  

### 3. **Simulated Flight Planning**  
- Self-contained flight simulator (`agents/flight_planner.py`) — no external flight API needed  
- Static IATA airport database with a ~90-entry nearest-airport map (e.g. Manali→Chandigarh, Munnar→Kochi, Agra→Delhi) including road distances, used when no direct flights are available at the origin/destination  
- Seeded random flight offers modeled on realistic Indian carriers, so results are deterministic for a given search  
- ±2-day flexible date search: if no flights are found on the exact date, suggests alternative nearby dates  
- Round-trip support, including return legs with stops  
- Displays:  
  - Airline, flight number, timings  
  - Departure & arrival airports  
  - Duration and pricing  

### 4. **Budget Calculator**  
- Accommodation type selection (Budget hostel to Luxury resort)  
- Returns a single estimated total budget (falls back to ₹50,000 if the agent can't produce one)  

### 5. **Itinerary Generator**  
- AI-generated day-by-day activity planning  
- Personalized based on user interests  
- Downloadable itinerary in Markdown format  

### 6. **Current Weather Conditions**  
- **OpenWeather API integration** (geocoding + current weather endpoint)  
- LLM-summarized conditions for the destination  
- Temperature, conditions, and recommendations  
- Note: this reflects **current** weather at query time, not a forecast for your actual travel dates  

## Technical Stack  

- **Frontend**: Streamlit (Python web framework)  
- **AI Agents**:  
  - **`openai/gpt-oss-20b`** (Groq) for destination, itinerary, and weather summarization  
  - **`llama-3.1-8b-instant`** (Groq) for budget estimation  
- **APIs**:  
  - **Groq API** (LLM inference)  
  - **OpenWeather API** (current weather data)  
- **Flight Data**: Local simulator — static airport database + seeded random offer generation, no external API  
- **Styling**: Custom CSS with modern UI components  
- **State Management**: Streamlit session state  

## Project Structure

Tour_Planner_Bot/
├── app.py # Streamlit entry point, step-by-step UI flow
├── agents/
│ ├── destination_agent.py # Destination recommendations (gpt-oss-20b)
│ ├── flight_planner.py # Flight simulator (AIRPORT_DB, NEARBY_AIRPORT_MAP, generate_mock_flights)
│ ├── budget_agent.py # Budget estimation (llama-3.1-8b-instant)
│ ├── itinerary_agent.py # Day-by-day itinerary generation (gpt-oss-20b)
│ └── weather_agent.py # OpenWeather lookup + summarization (gpt-oss-20b)
├── requirements.txt
├── .env # GROQ_API_KEY, OPENWEATHER_API_KEY
└── .devcontainer/ # Codespaces dev container config


## Installation  

1. Clone the repository:  
```bash  
   git clone https://github.com/Anveeksha15/Tour_Planner_Bot.git
   cd Tour_Planner_Bot
```  

2. Install dependencies:  
```bash  
   pip install -r requirements.txt  
```  
   > Note: `requirements.txt` currently still lists `amadeus`, `langgraph`, and `langchain_community`, which nothing in the codebase imports. Safe to remove if you want a leaner install.

3. Set up API keys:  
   - Obtain a **Groq API key** and an **OpenWeather API** key  
   - Add them to `.env` file:
 GROQ_API_KEY=your_api_key  
 OPENWEATHER_API_KEY=your_api_key

4. Run the application:  
```bash  
   streamlit run app.py  
```  

   You can also open this project in **GitHub Codespaces** — a dev container config is included for a ready-to-run environment.

## Usage  

1. **Define Travel Preferences**  
   - Enter dates, interests, and departure city  

2. **Browse AI-Recommended Destinations**  
   - Select from dynamically generated options  

3. **Check Flight Availability**  
   - Simulated flight options based on origin/destination airports  
   - If no direct flights exist, nearby airports are checked using the built-in distance map  
   - If nothing is available on your exact date, alternative dates within ±2 days are suggested  

4. **Set Budget & Generate Itinerary**  
   - Adjust accommodation type  
   - Get a detailed day-by-day plan  
   - Budget total is a single estimated figure (reference fallback: ₹50,000)  

5. **Check Weather Conditions**  
   - See current weather conditions for the destination (not a dated forecast)  

6. **Download Itinerary**  
   - Save as Markdown for offline use  


