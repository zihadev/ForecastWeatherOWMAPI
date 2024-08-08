# coding=utf-8
import streamlit as st
import pandas as pd

st.title("weather forecast for the next days".title())

place = st.text_input("Enter Place:", value = "Zabrze")

days = st.slider("Forecast Days:", min_value=1, max_value=5, help = "Select the number of forecasted days")

# List of options
options = ["Temperature", "Sky"]
# Create a selectbox
selected_option = st.selectbox("Select data to view:", options)
day_label = "day" if days == 1 else "days"
st.subheader(f"{selected_option} for the next {days} {day_label} for {place}")
