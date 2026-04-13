import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page config for professional look
st.set_page_config(page_title="Saudi Logistics Pro", page_icon="🇸🇦", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #ddd; }
    .status-box { padding: 20px; border-radius: 10px; background-color: #e9ecef; border-left: 5px solid #28a745; }
    </style>
    """, unsafe_allow_html=True)

# sidebar for Branding
with st.sidebar:
    st.image("https://img.icons8.com/color/96/delivery.png", width=100)
    st.title("Saudi Logistics")
    st.info("Quality Delivery across the Kingdom.")

# Dummy Data with Dates
# 'send_date': Kab bheja gaya | 'eta': Kab tak pahuchega
tracking_db = {
    "SA-2026-01": {
        "status": "In Transit", 
        "location": "Jeddah Hub", 
        "destination": "Riyadh", 
        "send_date": "2026-04-10",
        "eta": "2026-04-14",
        "update": "Departed from Jeddah Sorting Center"
    },
    "SA-2026-02": {
        "status": "Delivered", 
        "location": "Dammam", 
        "destination": "Dammam", 
        "send_date": "2026-04-05",
        "eta": "2026-04-08",
        "update": "Package delivered to customer"
    }
}

st.title("📦 Shipment Tracking System")
st.write("Apna tracking number neeche darj karein.")

# Layout for Search
col1, col2 = st.columns([2, 1])
with col1:
    track_id = st.text_input("Enter Tracking ID (Example: SA-2026-01):").strip()
with col2:
    st.write("##")
    search_btn = st.button("Track Order")

if search_btn:
    if track_id in tracking_db:
        data = tracking_db[track_id]
        
        st.markdown("---")
        
        # UI Highlights
        c1, c2, c3 = st.columns(3)
        c1.metric("Current Status", data["status"])
        c2.metric("Sending Date", data["send_date"])
        c3.metric("Estimated Arrival (ETA)", data["eta"])
        
        # Detailed Information Box
        st.markdown(f"""
        <div class="status-box">
            <h4>Live Update: {data['update']}</h4>
            <p><b>Current Location:</b> {data['location']} | <b>Destination:</b> {data['destination']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Timeline Visualizer
        st.write("### Delivery Progress")
        steps = ["Booked", "In Transit", "Out for Delivery", "Delivered"]
        current_idx = steps.index(data["status"]) if data["status"] in steps else 1
        
        # Simple Progress bar based on steps
        progress_val = (current_idx + 1) * 25
        st.progress(progress_val)
        
        st.write(f"**Timeline:** {' ➡️ '.join([f'**{s}**' if s == data['status'] else s for s in steps])}")

    else:
        st.error("❌ Invalid Tracking Number. Please verify and try again.")

# Footer Area
st.markdown("---")
st.caption("© 2026 Saudi Logistics Management | Jeddah, KSA")
