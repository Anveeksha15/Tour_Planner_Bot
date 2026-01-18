import os
import re
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
os.environ['GROQ_API_KEY'] = st.secrets["GROQ_API_KEY"]

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(model_name='Gemma2-9b-It')

def calculate_budget(destination, dates, accommodation_type, flight_location, interests, flight_cost=None):
    budget_prompt_template = """
    You are a smart travel budget calculator for Indian destinations. Calculate a realistic budget based on these inputs:

    **Trip Details:**
    - Destination: {destination}
    - Travel dates: {dates} (calculate duration)
    - Accommodation: {accommodation_type}
    - Departure: {flight_location}
    - Interests: {interests}
    {flight_cost_text}

    **Output Requirements:**
    - Return ONLY the total budget amount as a clean integer (no text, no symbols)
    - Example: 45000 (for ₹45,000)
    - Must be numeric only
    """

    flight_cost_text = f"- Flight Cost: ₹{flight_cost:,}" if flight_cost else ""

    prompt = ChatPromptTemplate.from_template(budget_prompt_template)
    chain = prompt | llm

    try:
        result = chain.invoke({
            "destination": destination,
            "dates": dates,
            "accommodation_type": accommodation_type,
            "flight_location": flight_location,
            "interests": interests,
            "flight_cost_text": flight_cost_text
        })
        
        # Extract pure numeric value
        budget_value = int(re.search(r'\d+', result.content).group())
        return budget_value
        
    except Exception as e:
        print(f"Budget calculation error: {str(e)}")
        return 50000  # Fallback value