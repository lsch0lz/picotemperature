from datetime import datetime

import streamlit as st
import pandas as pd

from utils.date import get_dates, filter_dates, DATE_TIME_STR

st.title("Pico Temperature")

df = pd.read_csv("/Users/lukasscholz/repositorys/picotemperature/app/data/temperature.csv",
                 names=["Date", "Temperature"], skiprows=[0])

with st.sidebar:
    date_picker = st.date_input("Date", [datetime.strptime(get_dates(df)[1], DATE_TIME_STR).date(),
                                         datetime.strptime(get_dates(df)[0], DATE_TIME_STR).date()])

try:
    st.line_chart(data=filter_dates(df, date_picker[0], date_picker[1]), x="Date", y="Temperature")
except IndexError:
    st.error("You must pick a start and end date")
    st.stop()
