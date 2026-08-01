import pandas as pd


def validate_dataframe(df: pd.DataFrame):

    report = {}

    report["Rows"] = df.shape[0]
    report["Columns"] = df.shape[1]
    report["Missing Values"] = int(df.isnull().sum().sum())
    report["Duplicate Rows"] = int(df.duplicated().sum())

    return report