# coding=utf-8
import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.title("weather forecast for the next days".title())

place = st.text_input("Enter Place:", value = "Zabrze")

days = st.slider("Forecast Days:", min_value=1, max_value=5, help = "Select the number of forecasted days")

# List of options
options = ["Temperature", "Sky"]
# Create a selectbox
selected_option = st.selectbox("Select data to view:", options)
day_label = "day" if days == 1 else "days"
st.subheader(f"{selected_option} for the next {days} {day_label} for {place}")


dates =['2022-25-10','2022-26-10','2022-27-10','2022-28-10','2022-29-10']
temperatures = [10,12,15,5,7]
temperatures = [i*random.randint(1,50)*days for i in temperatures]

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"Temperature(C)"})
st.plotly_chart(figure)
