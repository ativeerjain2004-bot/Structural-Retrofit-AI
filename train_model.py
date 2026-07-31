import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


DATASET = "data/retrofit_dataset.csv"

MODEL_PATH = "models/retrofitting_model.pkl"
SCALER_PATH = "models/scaler.pkl"
COLUMN_PATH = "models/model_columns.pkl"


def load_dataset():

    df = pd.read_csv(DATASET)

    X = df.drop("Recommended_Method", axis=1)
    y = df["Recommended_Method"]

    X = pd.get_dummies(X)

    return X, y


def preprocess(X):

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler


def train_model(X_train, y_train):

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def evaluate(model, X_test, y_test):

    prediction = model.predict(X_test)

    print("\nAccuracy : ", accuracy_score(y_test, prediction))
    print()
    print(classification_report(y_test, prediction))


def save(model, scaler, columns):

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(columns, COLUMN_PATH)


def main():

    X, y = load_dataset()

    columns = X.columns

    X_scaled, scaler = preprocess(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = train_model(X_train, y_train)

    evaluate(model, X_test, y_test)

    save(model, scaler, columns)

    print("\nTraining Completed Successfully")


if __name__ == "__main__":
    main()
