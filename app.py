import streamlit as st
import pandas as pd

st.title("Heart Disease Prediction")
st.write("A project to predict heart disease, and maximum heart rate on exercise")

df = pd.read_csv("data/processed/heart_clean.csv")
st.dataframe(df.head())
