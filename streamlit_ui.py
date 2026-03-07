import streamlit as st
import requests

st.title("🩺 AI Symptom Analyzer")

st.write("Enter your symptoms and the system will predict the category.")

symptoms = st.text_area("Describe your symptoms")

if st.button("Analyze"):

    if symptoms.strip() == "":
        st.warning("Please enter symptoms")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:5000/analyze",
                json={"text": symptoms}
            )

            result = response.json()

            st.success(f"Predicted Category: {result['predicted_category']}")

        except:
            st.error("API not running. Please start Flask server.")