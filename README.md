# Heart Failure Analysis

This project takes data from studies of 918 patients with and without a heart disease diagnosis, and uses it to investigate differences between patient groups with respect to heart disease diagnosis and maximal heart rate on exercise.  Two machine learning models were used: logistic regression to classify heart disease, and linear regression to predict maximum heart rate.

The project might be useful to beginner data analysts who want to see how to analyse group averages with a t-test, as detailed in the notebooks, and to visualise data in Streamlit with boxplots, as shown in the app.  The project shows how to incorporate a slider into the workflow to make a chart interactive.

The Streamlit app contains a data table showing the first five rows of patient data, an interactive histogram and a boxplot.  The histogram lets the user interact with it by limiting the upper and lower age bounds of the patients in the histogram using a slider widget.