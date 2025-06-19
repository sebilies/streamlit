import streamlit as st
import time
st.balloons()
st.subheader("Progress Status Example")
st.progress(10, text="Starting...")
st.subheader("wait for execution")
with st.spinner("Processing..."):
    time.sleep(5)  # Simulate a long-running process