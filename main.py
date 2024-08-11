# coding=utf-8
import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data
import os


def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux (posix systems)
    else:
        os.system('clear')


# Example usage
clear_terminal()
print("started")

st.markdown("## Weather Forecast for the Next Days".title())

place = st.text_input("Enter Place:", value="Zabrze")

days = st.slider("Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

# List of options
options = ["Temperature", "Sky"]
# Create a selectbox
selected_option = st.selectbox("Select data to view:", options)
day_label = "day" if days == 1 else "days"
st.subheader(f"{selected_option} for the next {days} {day_label} for {place}")

dates, temperatures = get_data(place, days, selected_option)

figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature(C)"})
st.plotly_chart(figure, on_select="rerun")
