import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(
    page_title="AI Greeting Card Assistant",
    page_icon="💌"
)

# Load API key securely
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("API Key not found! Please add it to secrets.toml")
    st.stop()

# Initialize model
model = genai.GenerativeModel("gemini-3-flash-preview")

# Title
st.title("💌 AI Greeting Card Assistant")

# Description
st.write("Create personalized greeting messages using AI!")

# Inputs
occasion = st.text_input("Enter the occasion (e.g., Birthday)")
recipient = st.text_input("Who is it for? (e.g., my friend)")
tone = st.selectbox(
    "Select tone",
    ["Funny", "Formal", "Heartfelt"]
)


# Button
if st.button("Generate Message"):

    # Validate input
    if not occasion or not recipient:
        st.warning("Please fill all fields!")
    else:
        # Prompt Engineering
        prompt = f"""
        Write a {tone.lower()} greeting message for {recipient} for the occasion of {occasion}.
        Make it engaging, meaningful, and well-written.
        """

        # Call Gemini
        response = model.generate_content(prompt)

        # Display result
        st.subheader("✨ Your AI-Generated Message:")
        st.write(response.text)