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

dates, temperatures, icons = get_data(place, days, selected_option)

figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature(C)"})
st.plotly_chart(figure, on_select="rerun")

# Create HTML for each icon
icon_html = [
    f'<img src="https://openweathermap.org/img/w/{icon}.png" style="width:50px;height:50px;">'
    for icon in icons
]

temperature = [f"{temperature} °C" for temperature in temperatures]
# Convert lists to a pandas DataFrame

# day = [f"{day}" for day in dates]
formatted_date = [day.strftime("%d %B %y, hour %H") for day in dates]

# Determine the number of columns you want in the grid
num_columns = 3
columns = st.columns(num_columns)

# Iterate over the data and place each in the grid
for index in range(len(formatted_date)):
    # Use modulo to decide which column to place the item in
    col = columns[index % num_columns]

    # Display content in the chosen column
    with col:
        st.markdown(icon_html[index], unsafe_allow_html=True)
        st.write(f"{temperatures[index]} °C")
        st.info(formatted_date[index])
