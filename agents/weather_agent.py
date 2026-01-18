import os
import requests
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

# Load environment variables
load_dotenv()
os.environ['GROQ_API_KEY'] = st.secrets["GROQ_API_KEY"]
OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]

# Initialize LLM
llm = ChatGroq(model_name="Gemma2-9b-It")

def get_city_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={OPENWEATHER_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if not data:
            return None, None
        return data[0]['lat'], data[0]['lon']
    except Exception as e:
        return None, None

def fetch_current_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={OPENWEATHER_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 429:
            return "⚠️ Weather API limit reached. Please try again later."
        if response.status_code != 200:
            return None
        return response.json()
    except Exception as e:
        return None

def weather_forecast(city):
    lat, lon = get_city_coordinates(city)
    if lat is None or lon is None:
        return f"❌ Could not find coordinates for city: {city}"

    weather_data = fetch_current_weather(lat, lon)
    if weather_data is None or isinstance(weather_data, str):
        return weather_data or "❌ Could not retrieve weather data."

    try:
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        description = weather_data["weather"][0]["description"].capitalize()
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        summary_text = (
            f"- Temperature: {temp}°C\n"
            f"- Feels Like: {feels_like}°C\n"
            f"- Condition: {description}\n"
            f"- Humidity: {humidity}%\n"
            f"- Wind Speed: {wind_speed} m/s"
        )

        # Chain LLM prompt
        summary_template = """
You are a travel assistant. Summarize the current weather conditions in {city} and give brief travel advice if necessary.
Give the answer in bullet points like a perfect weather application.

Current weather data:
{weather_data}
"""
        prompt = ChatPromptTemplate.from_template(summary_template)
        chain = prompt | llm

        return chain.invoke({
            "city": city,
            "weather_data": summary_text
        }).content

    except Exception as e:
        return f"❌ Weather processing failed: {str(e)}"

