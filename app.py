import streamlit as st
import pandas as pd

from predictor import predict
from expert_rules import recommend_using_rules


target_names = {
    0: "CFRP Wrap",
    1: "Concrete Jacketing",
    2: "GFRP Wrap",
    3: "Steel Plate Bonding"
}


st.set_page_config(
    page_title="AI Structural Retrofit Recommendation",
    layout="wide",
    page_icon="🏗️"
)

st.title("🏗️ AI Based Structural Rehabilitation Recommendation System")

st.write(
    "Predict the most suitable rehabilitation technique using "
    "structural condition, environmental exposure and budget constraints."
)

left, right = st.columns(2)

with left:

    st.subheader("Structural Parameters")

    length = st.number_input(
        "Beam Length (mm)",
        value=5000
    )

    width = st.number_input(
        "Beam Width (mm)",
        value=300
    )

    depth = st.number_input(
        "Beam Depth (mm)",
        value=450
    )

    strength = st.slider(
        "Concrete Strength (MPa)",
        10.0,
        50.0,
        25.0
    )

    crack = st.slider(
        "Maximum Crack Width (mm)",
        0.0,
        5.0,
        0.5
    )

    loss = st.slider(
        "Capacity Loss (%)",
        0.0,
        60.0,
        10.0
    )

with right:

    st.subheader("Damage Information")

    damage = st.selectbox(
        "Damage Type",
        [
            "Flexural",
            "Shear",
            "Corrosion"
        ]
    )

    exposure = st.selectbox(
        "Exposure Condition",
        [
            "Normal",
            "Aggressive",
            "Fire-prone"
        ]
    )

    settlement = st.selectbox(
        "Differential Settlement",
        [
            "No",
            "Yes"
        ]
    )

    dynamic = st.selectbox(
        "Dynamic Loading",
        [
            "Low",
            "High"
        ]
    )

    seismic = st.selectbox(
        "Seismic Zone",
        [
            "Zone II",
            "Zone III",
            "Zone IV",
            "Zone V"
        ]
    )

    budget = st.selectbox(
        "Budget",
        [
            "Low",
            "Medium",
            "High"
        ]
    )


if st.button("Predict Retrofit Method"):

    sample = {

        "Length_mm": length,

        "Width_mm": width,

        "Depth_mm": depth,

        "Nominal_Grade_MPa": 25,

        "Actual_Strength_MPa": strength,

        "Damage_Type": damage,

        "Max_Crack_Width_mm": crack,

        "Capacity_Loss_Pct": loss,

        "Exposure_Condition": exposure,

        "Differential_Settlement": settlement,

        "Dynamic_Load_Freq": dynamic,

        "Seismic_Zone": seismic,

        "Budget_Constraint": budget
    }

    prediction, probability = predict(sample)

    ml_result = target_names[prediction]

    rule_result = recommend_using_rules(sample)

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Machine Learning Recommendation",
            ml_result
        )

    with c2:

        st.metric(
            "Engineering Rule Recommendation",
            rule_result
        )

    st.subheader("Prediction Confidence")

    probability_df = pd.DataFrame({

        "Technique": list(target_names.values()),

        "Probability": probability

    })

    st.bar_chart(
        probability_df.set_index("Technique")
    )

    st.subheader("Input Summary")

    st.dataframe(
        pd.DataFrame([sample])
    )

    if ml_result == rule_result:

        st.success(
            "Machine learning prediction agrees with engineering rules."
        )

    else:

        st.warning(
            "Engineering rules suggest a different retrofit strategy. Review both recommendations before final selection."
        )
