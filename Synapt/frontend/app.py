import streamlit as st
import requests

st.title("Offline Multi-Agent Travel Planning System")

origin = st.text_input("Origin")
destination = st.text_input("Destination")
dates = st.text_input("Dates (comma-separated)")
budget = st.number_input("Budget (INR)", min_value=0)
preferences = st.text_input("Preferences (comma-separated)")
email = st.text_input("Contact Email")

if st.button("Plan Trip"):
    request_data = {
        "origin": origin,
        "destination": destination,
        "dates": dates.split(","),
        "budget": budget,
        "preferences": preferences.split(","),
        "email": email
    }
    response = requests.post("http://localhost:8000/planner/process", json=request_data)
    st.json(response.json())

if st.button("Download PDF"):
    # Logic to download PDF
    pass

if st.button("Download ICS"):
    # Logic to download ICS
    pass
