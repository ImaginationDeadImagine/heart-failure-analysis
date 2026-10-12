import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Heart Disease Prediction")
st.write("A project to predict heart disease, and maximum heart rate on exercise")

df = pd.read_csv("data/processed/heart_clean.csv")
st.dataframe(df.head())
st.subheader("")

fig, ax = plt.subplots()
sns.histplot(data=df, x="Age", ax=ax)
ax.set_title("Age distribution of patients")
ax.set_xlabel("Age")
ax.set_ylabel("Number of patients")
st.pyplot(fig)

st.write("The plot shows the age distribution of all patients in the study.")