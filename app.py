import streamlit as st
import requests
import random
import time

st.title("Account Registration Tester")

st.write("This tool will test account registration on your site.")

# --- Input fields ---
email_input = st.text_input("Email (optional, leave blank for automatic)")
password_input = st.text_input("Password", value="TestPass123!")
name_input = st.text_input("Name", value="Tester")

target_site = st.text_input("Your Site URL", value="https://your-site.example")
register_path = st.text_input("Register Path", value="/register")

# --- User agents for randomization ---
user_agents = [
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) Chrome/115.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/116.0 Safari/537.36"
]

# --- Register button ---
if st.button("Register"):
    st.write("Processing...")

    # If email blank, generate one
    if not email_input:
        email_input = f"test+{int(time.time()*1000)}@example.com"

    headers = {"User-Agent": random.choice(user_agents)}
    payload = {"email": email_input, "password": password_input, "name": name_input}

    try:
        response = requests.post(target_site + register_path, data=payload, headers=headers, timeout=30)
        st.success(f"Status code: {response.status_code}")
        st.code(response.text[:400])
    except Exception as e:
        st.error(f"Error: {e}")
      Add Streamlit registration tester
