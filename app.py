import streamlit as st

# Page configuration
st.set_page_config(page_title="Saudi Logistics Pro", page_icon="📦", layout="wide")

# COMPLETE UI FIX - Dono Light aur Dark theme mein sahi dikhega
st.markdown("""
    <style>
    /* 1. Main App Background */
    .stApp {
        background-color: #f0f2f6;
    }

    /* 2. Metric Cards Fix (White Background + Dark Text) */
    [data-testid="stMetric"] {
        background-color: #ffffff !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        border: 1px solid #e1e4e8 !important;
    }

    /* 3. Text Color Fix inside Metrics */
    [data-testid="stMetricLabel"] {
        color: #444444 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }
    [data-testid="stMetricValue"] {
        color: #111111 !important;
        font-weight: bold !important;
    }

    /* 4. Live Update Box Styling */
    .status-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        border-left: 8px solid #00843D; /* Saudi Green */
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    .status-header {
        color: #00843D;
        margin-bottom: 10px;
        font-size: 22px;
        font-weight: bold;
    }

    .status-text {
        color: #333333;
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- App Content ---
st.title("🚚 Saudi Courier Tracking")
st.write("Enter your shipment details below:")

# Input field
track_id = st.text_input("Tracking Number:", placeholder="SA-2026-XXXX")

# Dummy data logic (Testing ke liye)
if track_id:
    # Example values
    status = "In Transit"
    s_date = "2026-04-10"
    e_date = "2026-04-14"
    update_msg = "Departed from Jeddah Sorting Center"
    current_loc = "Jeddah Hub"
    dest = "Riyadh"

    st.markdown("---")

    # Metrics Layout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Current Status", value=status)
    with col2:
        st.metric(label="Sending Date", value=s_date)
    with col3:
        st.metric(label="Estimated Arrival", value=e_date)

    # Status Box
    st.markdown(f"""
        <div class="status-card">
            <div class="status-header">Live Update: {update_msg}</div>
            <div class="status-text">
                <b>Current Location:</b> {current_loc} <br>
                <b>Destination:</b> {dest}
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("Please enter a tracking number to see the result.")
