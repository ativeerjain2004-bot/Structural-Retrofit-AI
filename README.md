# AI-Based Structural Rehabilitation Recommendation System

This project is a decision-support tool that recommends suitable structural rehabilitation techniques using machine learning and engineering rules.

## Features

- Predicts retrofit method from structural parameters
- Random Forest Classifier
- Rule-based engineering validation
- Streamlit web interface
- Probability visualization

## Technologies

- Python
- Streamlit
- Pandas
- Scikit-Learn
- Joblib

## Project Structure

```
app.py
train_model.py
predictor.py
preprocessing.py
expert_rules.py
data/
models/
```

## Installation

```bash
pip install -r requirements.txt
```

## Train

```bash
python train_model.py
```

## Run

```bash
streamlit run app.py
```
