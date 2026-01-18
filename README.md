# Travel Buddy - Smart Travel Planning Assistant  

## Overview  

Travel Buddy is an AI-powered travel planning assistant that helps users plan their perfect trip within India. The application guides users through a step-by-step process, from selecting destinations to generating detailed itineraries, using real-time flight data and weather forecasts.  

Powered by **Gemma2-9b-It** for AI-driven recommendations, **Amadeus API** for live flight searches, and **OpenWeather API** for accurate weather forecasts, Travel Buddy ensures a seamless and data-driven travel planning experience.  

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
- Uses **Gemma2-9b-It** for personalized recommendations  

### 3. **Real-Time Flight Planning**  
- **Amadeus API Integration** for live flight data  
- Searches nearby airports if no direct flights are available  
- Automatically suggests flights from the next nearest airport  
- Displays:  
  - Airline, flight number, timings  
  - Departure & arrival airports  
  - Duration and pricing  

### 4. **Budget Calculator**  
- Accommodation type selection (Budget hostel to Luxury resort)  
- Comprehensive budget estimation including:  
  - Flights (real-time pricing)  
  - Daily expenses  
  - Activities based on interests  

### 5. **Itinerary Generator**  
- AI-generated day-by-day activity planning  
- Personalized based on user interests  
- Downloadable itinerary in Markdown format  

### 6. **Accurate Weather Forecast**  
- **OpenWeather API integration** for real-time weather data  
- Forecast for travel dates  
- Temperature, conditions, and recommendations  

## Technical Stack  

- **Frontend**: Streamlit (Python web framework)  
- **AI Agents**:  
  - **Gemma2-9b-It** for destination, budget, and itinerary generation  
- **APIs**:  
  - **Amadeus API** (Flight search & real-time pricing)  
  - **OpenWeather API** (Weather forecasts)  
- **Styling**: Custom CSS with modern UI components  
- **State Management**: Streamlit session state  

## Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/travel-buddy.git  
   cd travel-buddy  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Set up API keys:  
   - Obtain **Amadeus API** & **OpenWeather API** keys  
   - Add them to `.env` file:  
     ```  
     AMADEUS_API_KEY=your_api_key  
     OPENWEATHER_API_KEY=your_api_key  
     ```  

4. Run the application:  
   ```bash  
   streamlit run app.py  
   ```  

## Usage  

1. **Define Travel Preferences**  
   - Enter dates, interests, and departure city  

2. **Browse AI-Recommended Destinations**  
   - Select from dynamically generated options  

3. **Check Flight Availability**  
   - Real-time flight options with alternative airports if needed  

4. **Set Budget & Generate Itinerary**  
   - Adjust accommodation type  
   - Get a detailed day-by-day plan  

5. **Check Weather Forecast**  
   - See weather predictions for travel dates  

6. **Download Itinerary**  
   - Save as Markdown for offline use  

## Customization  

- Modify `app.py` to adjust AI prompts  
- Change CSS in the `<style>` section for different themes  
- Extend flight search logic for more airport alternatives  

## Future Enhancements  

✅ **Done:**  
- Real-time flight data (Amadeus API)  
- Dynamic weather forecasts (OpenWeather API)  
- AI-driven recommendations (Gemma2-9b-It)  

🔜 **Planned:**  
- Hotel & activity booking integration  
- Multi-city trip support  
- User accounts to save trip history  

## License  

[MIT License] - Free for personal and commercial use.  

---  
