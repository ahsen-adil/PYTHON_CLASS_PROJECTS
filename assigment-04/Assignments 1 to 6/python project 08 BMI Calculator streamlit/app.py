import streamlit as st
import pandas as pd

# App ka title
st.title("BMI Calculator")

# User inputs ke liye sliders
height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# BMI result dikhana
st.write(f"Your BMI is **{bmi:.2f}**")

# BMI Categories
st.write("### BMI Categories ###")
st.write("- **Underweight**: BMI less than 18.5")
st.write("- **Normal weight**: BMI between 18.5 and 24.9")
st.write("- **Overweight**: BMI between 25 and 29.9")
st.write("- **Obesity**: BMI 30 or greater")