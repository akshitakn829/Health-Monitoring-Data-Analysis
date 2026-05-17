import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Health Monitoring Dashboard")

data = {
    "Name":["Asha","Rahul","Priya","Kiran","Arun"],
    "Age":[22,35,28,45,50],
    "HeartRate":[72,88,76,95,102],
    "BMI":[21.5,27.8,23.0,30.2,32.1]
}

df = pd.DataFrame(data)

st.subheader("Patient Health Data")
st.dataframe(df)

st.write("Average Heart Rate:", df["HeartRate"].mean())
st.write("Average BMI:", df["BMI"].mean())

fig = px.bar(df, x="Name", y="HeartRate",
             title="Heart Rate Monitoring")

st.plotly_chart(fig)

st.success("Health Monitoring System Active")

