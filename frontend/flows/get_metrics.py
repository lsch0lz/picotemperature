from pandas import DataFrame


def calculate_mean(dataframe: DataFrame) -> float:
    return dataframe.loc[:, "Temperature"].mean()


def calculate_median(dataframe: DataFrame) -> float:
    return dataframe.loc[:, "Temperature"].median()


def calculate_highest_temperature(dataframe: DataFrame) -> float:
    return dataframe.loc[:, "Temperature"].max()


def calculate_lowest_temperature(dataframe: DataFrame) -> float:
    return dataframe.loc[:, "Temperature"].min()


def get_metrics(dataframe: DataFrame):
    return calculate_mean(dataframe), calculate_median(dataframe), calculate_highest_temperature(
        dataframe), calculate_lowest_temperature(dataframe)
