import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
os.environ['GROQ_API_KEY'] = st.secrets["GROQ_API_KEY"]

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(model_name='Gemma2-9b-It')

def destination(preferences, budget, interests):
    generic_template = (
       """You are a travel assistant. Based on the following user inputs:
        - Preferred region(s): {preferences}
        - Interests/activities: {interests}
        - Total budget in INR: {budget}

        Suggest 3 to 5 tourist destinations **within India** that match the given preferences and interests. 
        Ensure that the suggested destinations are **budget-friendly** and suitable for the specified interests. 

        Only return the names of the destinations in **bullet points**. Do not include any descriptions, explanations, or additional information. Stick to this point. Dont even give any text like here you go. Just the destinations are expected."""
    )

    prompt = ChatPromptTemplate.from_template(generic_template)
    chain = prompt | llm

    try:
        result = chain.invoke({
            "preferences": preferences,
            "budget": budget,
            "interests": interests
        })
        return result.content
    except Exception as e:
        return f"❌ Destination recommendation failed: {str(e)}"