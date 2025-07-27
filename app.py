import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("🧠 AI Task Category Classifier")

# User input
user_input = st.text_input("Enter your task description:")

# Predict
if st.button("Predict Category"):
    if user_input.strip() == "":
        st.warning("Please enter a task description.")
    else:
        prediction = model.predict([user_input])
        st.success(f"Predicted Category: {prediction[0]}")
# Set a light lavender background and style the app
st.markdown("""
    <style>
    .stApp {
        background-color: #E6E6FA;  /* Light lavender */
        font-family: 'Segoe UI', sans-serif;
        padding: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    .stButton > button {
        color: white;
        background-color: #B57EDC;  /* Medium lavender */
        border: none;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #A36BCF;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)
