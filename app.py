import streamlit as st

# Page config
st.set_page_config(page_title="Saudi Logistics Pro", page_icon="📦", layout="wide")

# Fixed CSS - Text colors and Backgrounds defined
st.markdown("""
    <style>
    /* Main background color */
    .stApp { background-color: #f4f7f6; }
    
    /* Metric Card Styling with fixed text color */
    [data-testid="stMetric"] {
        background-color: #ffffff !important;
        padding: 20px !important;
        border-radius: 15px !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.05) !important;
    }
    
    /* Force label and value to be dark/visible */
    [data-testid="stMetricLabel"] { color: #555555 !important; font-weight: bold !important; }
    [data-testid="stMetricValue"] { color: #1a1a1a !important; }

    /* Live Update Box with clear text */
    .status-box {
        padding: 25px;
        border-radius: 12px;
        background-color: #ffffff;
        border-left: 8px solid #00813d; /* Saudi Green color */
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
        color: #333333 !important;
    }
    
    h1, h2, h3, h4 { color: #1a1a1a !important; }
    </style>
    """, unsafe_allow_html=True)

# --- Baki logic wahi rahega jo pehle tha ---
st.title("📦 Saudi Shipment Tracker")

# Dummy Data for testing
data = {
    "status": "In Transit", 
    "send_date": "2026-04-10",
    "eta": "2026-04-14",
    "update": "Departed from Jeddah Sorting Center",
    "location": "Jeddah Hub",
    "destination": "Riyadh"
}

# Layout Improvement
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Current Status", data["status"])
with c2:
    st.metric("Sending Date", data["send_date"])
with c3:
    st.metric("Estimated Arrival", data["eta"])

# Status Box Fix
st.markdown(f"""
    <div class="status-box">
        <h3 style="margin-top:0;">Live Update: {data['update']}</h3>
        <p style="font-size:18px;"><b>Current Location:</b> {data['location']} <br> 
        <b>Final Destination:</b> {data['destination']}</p>
    </div>
    """, unsafe_allow_html=True)
