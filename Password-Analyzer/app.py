import streamlit as st
from zxcvbn import zxcvbn
import joblib
import requests
import hashlib

st.set_page_config(page_title="Password Analyzer", page_icon="🔐")

st.title("🔐 Password Strength Analyzer")

# Load ML model
model = joblib.load("password_model.pkl")

def extract_features(pw):
    return [
        len(pw),
        sum(c.isdigit() for c in pw),
        sum(c.isupper() for c in pw),
        sum(not c.isalnum() for c in pw)
    ]

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

password = st.text_input("Enter Password", type="password")

if password:
    # zxcvbn strength
    result = zxcvbn(password)
    score = result['score']

    levels = ["Very Weak ❌", "Weak ⚠️", "Fair 🟡", "Strong 💪", "Very Strong 🔥"]
    st.subheader(f"Strength: {levels[score]}")
    st.progress((score + 1) / 5)

    # ML Prediction
    features = [extract_features(password)]
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("🧠 ML Model: Strong Password")
    else:
        st.error("🧠 ML Model: Weak Password")

    # Breach check
    breach_count = check_pwned(password)
    if breach_count:
        st.error(f"⚠️ Found in {breach_count} breaches!")
    else:
        st.success("✅ Not found in known breaches")

    # Suggestions
    if result['feedback']['suggestions']:
        st.subheader("Suggestions:")
        for s in result['feedback']['suggestions']:
            st.write(f"- {s}")