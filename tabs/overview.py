import streamlit as st

def render(time_range, time_range_query_map):
    st.header("Overview")
    
    # Logic for DoS Overview
    if st.session_state.dashboard == "DoS":
        st.write(f"Displaying DoS overview for the last {time_range_query_map[time_range]}")
        # Add DoS-specific metrics here, e.g., attack count, anomaly rate, etc.
    
    # Logic for DNS Overview
    elif st.session_state.dashboard == "DNS":
        st.write(f"Displaying DNS overview for the last {time_range_query_map[time_range]}")
        # Add DNS-specific metrics here, e.g., DNS request count, anomaly rate, etc.

