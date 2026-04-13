import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Saudi Courier Tracking", page_icon="🚚", layout="centered")

# Custom CSS for RTL and Styling
st.markdown("""
    <style>
    .main { text-align: right; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Dummy Data - Real system mein ye Database (SQL/Google Sheets) se aayega
tracking_data = {
    "1001": {"status": "In Transit", "location": "Jeddah", "destination": "Riyadh", "update": "Arrived at Sorting Center"},
    "1002": {"status": "Delivered", "location": "Dammam", "destination": "Dammam", "update": "Handed to recipient"},
    "1003": {"status": "Out for Delivery", "location": "Mecca", "destination": "Mecca", "update": "With courier driver"},
    "1004": {"status": "Processing", "location": "Medina", "destination": "Abha", "update": "Package scanned at warehouse"}
}

# UI Header
st.title("🚚 Saudi Courier Service")
st.subheader("Track Your Shipment / اپنا پارسل ٹریک کریں")

# Input Section
track_id = st.text_input("Enter Tracking Number (e.g., 1001):", placeholder="Type here...")

if st.button("Track Status"):
    if track_id in tracking_data:
        data = tracking_data[track_id]
        
        # Display Results
        st.success(f"Shipment Found!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Status", data["status"])
            st.write(f"**Current Location:** {data['location']}")
        with col2:
            st.metric("Destination", data["destination"])
            st.write(f"**Last Update:** {data['update']}")
        
        # Progress Bar logic
        steps = {"Processing": 25, "In Transit": 50, "Out for Delivery": 75, "Delivered": 100}
        progress = steps.get(data["status"], 0)
        st.progress(progress)
        
    else:
        st.error("Invalid Tracking Number. Please check and try again.")

# Footer
st.markdown("---")
st.caption("Powered by Streamlit | Saudi Arabia Logistics Support")
