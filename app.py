import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Heart Disease and Relation to Maximum Heart Rate")
st.write("Exploring heart disease and maximum heart rate on exercise")

st.write("The question the app explores is whether there is a difference in average maximum heart rate on exercise between groups of patients with or without heart disease.")

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

st.subheader("Maximum Heart Rate by Heart Disease Category")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="HeartDisease", y="MaxHR", ax=ax)
ax.set_title("Maximum Heart Rate by Heart Disease Category")
ax.set_xlabel("Heart Disease Category (0 = No heart disease, 1 = Heart disease)")
ax.set_ylabel("Maximum heart rate (beats per minute)")
st.pyplot(fig)

st.write("The boxplot shows that the middle line of box 0 is above the top edge of box 1.  In other words, the median for patients without heart disease is above the 75th percentile for patients with heart disease.  Therefore, patients with heart disease tend to reach a lower maximum heart rate.")

st.caption("Contains information from [Heart Failure Prediction Dataset] (https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/), which is made available here under the [Open Data Commons Open Database License (ODbL) v1.0] (https://opendatacommons.org/licenses/odbl/1-0/).")
