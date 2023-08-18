from datetime import datetime

import streamlit as st
import pandas as pd
import pathlib
import os

from utils.date import get_dates, filter_dates, DATE_TIME_STR
from flows.get_metrics import get_metrics


st.title("Pico Temperature")


df = pd.read_csv(os.path.join(pathlib.Path(__file__).parents[1], "app/data/temperature.csv"),
                 names=["Date", "Temperature"], skiprows=[0])

with st.sidebar:
    date_picker = st.date_input("Date", [datetime.strptime(get_dates(df)[1], DATE_TIME_STR).date(),
                                         datetime.strptime(get_dates(df)[0], DATE_TIME_STR).date()])
    show_metrics = st.checkbox("Show Metrics")

try:
    st.line_chart(data=filter_dates(df, date_picker[0], date_picker[1]), x="Date", y="Temperature")

    if show_metrics:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Average Temperature", value=f"{get_metrics(filter_dates(df, date_picker[0], date_picker[1]))[0]} \N{DEGREE SIGN}C")
        col2.metric(label="Median Temperature", value=f"{get_metrics(filter_dates(df, date_picker[0], date_picker[1]))[1]} \N{DEGREE SIGN}C")
        col3.metric(label="Highest Temperature", value=f"{get_metrics(filter_dates(df, date_picker[0], date_picker[1]))[2]} \N{DEGREE SIGN}C")
        col4.metric(label="Lowest Temperature", value=f"{get_metrics(filter_dates(df, date_picker[0], date_picker[1]))[3]} \N{DEGREE SIGN}C")
except IndexError:
    st.error("You must pick a start and end date")
    st.stop()


