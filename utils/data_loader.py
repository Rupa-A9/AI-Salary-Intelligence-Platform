import pandas as pd


def load_csv(uploaded_file):
    """
    Reads uploaded CSV and returns DataFrame.
    """

    if uploaded_file is None:
        return None

    df = pd.read_csv(uploaded_file)

    return df