import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Heart Disease Prediction")
st.write("Prediction of heart disease, and maximum heart rate on exercise")

df = pd.read_csv("data/processed/heart_clean.csv")
st.dataframe(df.head())
st.subheader("Age distribution")

# slider
low, high = st.slider("Age range", int(df["Age"].min()), int(df["Age"].max()), (int(df["Age"].min()), int(df["Age"].max())))
filtered = df[(df["Age"] >= low) & (df["Age"] <= high)]

fig, ax = plt.subplots()
sns.histplot(data=filtered, x="Age", ax=ax)
ax.set_title("Age distribution of patients")
ax.set_xlabel("Age")
ax.set_ylabel("Number of patients")
st.pyplot(fig)

st.write("The plot shows all patients in the selected age range.")
st.write("Number of patients in the chart:", len(filtered))
