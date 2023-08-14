import streamlit as st
import pandas as pd

st.title("Pico Temperature")

df = pd.read_csv("/Users/lukasscholz/repositorys/picotemperature/app/data/temperature.csv", names=["Date", "Temperature"], skiprows=[0])
st.line_chart(data=df, x="Date", y="Temperature")
