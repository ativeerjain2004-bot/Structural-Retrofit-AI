import joblib

from preprocessing import prepare_input

MODEL_PATH = "models/retrofitting_model.pkl"

model = joblib.load(MODEL_PATH)


def predict(user_input):

    processed = prepare_input(user_input)

    prediction = model.predict(processed)[0]

    probability = model.predict_proba(processed)[0]

    return prediction, probability
