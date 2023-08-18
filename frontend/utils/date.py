from pandas import DataFrame
from prefect import task, flow

DATE_TIME_STR = "%Y-%m-%d"


def get_dates(dataframe: DataFrame) -> tuple[str, str]:
    df_dates = dataframe["Date"].tolist()
    df_dates_lowest = df_dates[0]
    df_dates_highest = df_dates[-1]
    return df_dates_lowest, df_dates_highest


def filter_dates(dataframe: DataFrame, date_from, date_to) -> DataFrame:
    return dataframe[(dataframe["Date"] >= date_from.strftime(DATE_TIME_STR)) & (
                dataframe["Date"] <= date_to.strftime(DATE_TIME_STR))]
