import joblib
import pandas as pd


COLUMN_PATH = "models/model_columns.pkl"
SCALER_PATH = "models/scaler.pkl"


def prepare_input(user_input):

    columns = joblib.load(COLUMN_PATH)
    scaler = joblib.load(SCALER_PATH)

    df = pd.DataFrame([user_input])

    df = pd.get_dummies(df)

    df = df.reindex(columns=columns, fill_value=0)

    scaled = scaler.transform(df)

    return scaled
