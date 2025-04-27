import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("disconnect_risk_model.pkl")


# Set page config
st.set_page_config(
    page_title="Virgin Media Disconnection Risk Predictor",
    page_icon=":satellite:",  # optional
    layout="centered"
)

# Custom CSS for Virgin Media theme
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #C70039, #FF5733);
        color: white;
    }
    .stButton>button {
        background-color: #FF5733;
        color: white;
        border: None;
    }
    .stSlider>div>div>div>div {
        background: #FF5733;
    }
    .stSelectbox>div>div>div {
        background: #FF5733;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# App title
st.title("Virgin Media Disconnection Risk Predictor")
st.markdown("#### Fill in the details below to check the risk of network disconnection.")

# Dropdown options
download_speed_options = [50, 100, 200, 500, 1000]
latency_options = [10, 20, 50, 100]
packet_loss_options = [0.0, 0.1, 0.5, 1.0, 5.0]

# Input fields
download_speed = st.selectbox("Download Speed (Mbps)", options=download_speed_options, index=1)
custom_download = st.number_input("Or type a custom Download Speed (Mbps)", min_value=0.0)

latency = st.selectbox("Latency (ms)", options=latency_options, index=0)
custom_latency = st.number_input("Or type a custom Latency (ms)", min_value=0.0)

packet_loss = st.selectbox("Packet Loss (%)", options=packet_loss_options, index=0)
custom_packet_loss = st.number_input("Or type a custom Packet Loss (%)", min_value=0.0)

# Hour + AM/PM
hour = st.slider("Hour (0–11)", 0, 11, 6)
ampm = st.selectbox("AM or PM", options=["AM", "PM"])

# Adjust hour based on AM/PM
hour_24 = hour if ampm == "AM" else hour + 12

# Month
month = st.slider("Month (1–12)", 1, 12, 6)

# Use custom values if user types them
final_download_speed = custom_download if custom_download > 0 else download_speed
final_latency = custom_latency if custom_latency > 0 else latency
final_packet_loss = custom_packet_loss if custom_packet_loss > 0 else packet_loss

# Predict button
if st.button("Predict Disconnection Risk"):
    input_data = pd.DataFrame({
        'Download Speed (Mbps)': [final_download_speed],
        'Latency (ms)': [final_latency],
        'Packet Loss (%)': [final_packet_loss],
        'hour': [hour_24],
        'month': [month]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Disconnection Detected!")
    else:
        st.success("✅ Low Risk of Disconnection. Network looks stable!")

