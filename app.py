import streamlit as st
import joblib
import pandas as pd
import json
import requests


# Load model and encoders
model = joblib.load("skip_predictor_model.pkl")
encoder = joblib.load("platform_encoder.pkl")
feature_order = joblib.load("feature_order.pkl")

# Page configuration
st.set_page_config(page_title="🎵 Spotify Skip Predictor", page_icon="🎧", layout="centered")


# Page title
st.title("🎵 Spotify Skip Predictor")





st.markdown("""
<style>
/* Background Image */
.stApp {
    background-image: url("https://images.pexels.com/photos/16100371/pexels-photo-16100371.jpeg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Top-right Header */
#top-header {
    position: fixed;
    top: 80px;  /* 👈 Yahi line hai jo update karni thi */
    right: 20px;
    background-color: rgba(0,0,0,0.5);
    padding: 14px 18px;
    border-radius: 8px;
    color: white;
    font-size: 18px;
    font-weight: bold;
    z-index: 90;
}

/* Bottom-left Footer */
#bottom-footer {
    position: fixed;
    bottom: 10px;
    left: 20px;
    background-color: rgba(0,0,0,0.5);
    padding: 6px 14px;
    border-radius: 6px;
    color: white;
    font-size: 14px;
    z-index: 100;
}
</style>

<div id="top-header">Respected Sir Shahzaib & Sir Ali Hamza</div>
<div id="bottom-footer">Developed by Faraz Hussain</div>
""", unsafe_allow_html=True)



# Title
st.markdown("<div class='title'>🎧 Spotify Song Skip Predictor</div>", unsafe_allow_html=True)

# Animation


# Prediction form
with st.form("predict_form"):
    st.markdown("### 🔍 Enter Listening Session Info")

    platform = st.selectbox("Select Platform:", options=encoder.classes_)
    ms_played = st.slider("Milliseconds Played", 0, 300000, 30000, step=1000)

    predict_button = st.form_submit_button("🚀 Predict")

# Predict and display
if predict_button:
    # Encode input
    encoded_platform = encoder.transform([platform])[0]
    input_df = pd.DataFrame([[encoded_platform, ms_played]], columns=feature_order)

    # Predict
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][prediction]

    if prediction == 1:
        st.markdown(f"<div class='result' style='color: #e53935;'>❌ Skipped (Confidence: {prob:.2%})</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result' style='color: #43a047;'>✅ Played (Confidence: {prob:.2%})</div>", unsafe_allow_html=True)




