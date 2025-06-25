import streamlit as st
from dos_dashboard import dos_dashboard
from dns_dashboard import dns_dashboard

# --- Set Page Configuration ---
st.set_page_config(page_title="Unified Anomaly Detection Dashboard", layout="wide")

# --- Sidebar Settings ---
time_range_query_map = {
    "Last 30 min": "-30m",
    "Last 1 hour": "-1h",
    "Last 24 hours": "-24h",
    "Last 7 days": "-7d",
    "Last 14 days": "-14d",
    "Last 30 days": "-30d"
}
time_range = st.sidebar.selectbox("Time Range", list(time_range_query_map.keys()), index=2)
thresh = st.sidebar.slider("Anomaly Threshold", 0.01, 1.0, 0.1, 0.01)
highlight_color = st.sidebar.selectbox("Highlight Color", ["Red", "Orange", "Yellow", "Green", "Blue"], index=3)
alerts_enabled = st.sidebar.checkbox("Enable Discord Alerts", value=True)

# --- Sidebar Toggle for Dashboard Type ---
dashboard_type = st.sidebar.radio(
    "Select Dashboard",
    ("DNS Anomaly Detection", "DoS Anomaly Detection"),
    index=0  # Default to DNS Anomaly Detection
)

# --- State Initialization ---
if "predictions" not in st.session_state:
    st.session_state.predictions = []
if "attacks" not in st.session_state:
    st.session_state.attacks = []

# --- Unified Tabs for Both Dashboards ---
tabs = st.tabs(["Overview", "Live Stream", "Manual Entry", "Metrics", "Historical Data"])

# --- Render Dashboard Based on the Selected Type (DNS vs DoS) ---
if dashboard_type == "DNS Anomaly Detection":
    with tabs[0]:
        dns_dashboard.render_overview(time_range, time_range_query_map)
    with tabs[1]:
        dns_dashboard.render_live_stream(thresh, highlight_color, alerts_enabled)
    with tabs[2]:
        dns_dashboard.render_manual_entry()
    with tabs[3]:
        dns_dashboard.render_metrics(thresh)
    with tabs[4]:
        dns_dashboard.render_historical_data(thresh, highlight_color)

elif dashboard_type == "DoS Anomaly Detection":
    with tabs[0]:
        dos_dashboard.render_overview(time_range, time_range_query_map)
    with tabs[1]:
        dos_dashboard.render_live_stream(thresh, highlight_color, alerts_enabled)
    with tabs[2]:
        dos_dashboard.render_manual_entry()
    with tabs[3]:
        dos_dashboard.render_metrics(thresh)
    with tabs[4]:
        dos_dashboard.render_historical_data(thresh, highlight_color)

