# Heart Failure Analysis

This project takes data from studies of 918 patients with and without a heart disease diagnosis, and uses it to investigate differences between patient groups with respect to heart disease diagnosis and maximal heart rate on exercise.  Two machine learning models were used: logistic regression to classify heart disease, and linear regression to predict maximum heart rate.

The project might be useful to beginner data analysts who want to see how to analyse group averages with a t-test, as detailed in the notebooks, and to visualise data in Streamlit with boxplots, as shown in the app.  The project shows how to incorporate a slider into the workflow to make a chart interactive.

The Streamlit app contains a data table showing the first five rows of patient data, an interactive histogram and a boxplot.  The histogram lets the user interact with it by limiting the upper and lower age bounds of the patients in the histogram using a slider widget.

## Live Dashboard

🔗 [View the deployed Streamlit app](https://your-app-name.onrender.com)

*Note: this app is hosted on Render's free tier. If it has been idle for 15 minutes, it can take about a minute to wake up.*

## Dataset

- **Source:** Heart Failure Prediction Dataset by fedesoriano on Kaggle (https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/)
- **Licence:** Open Data Commons Open Database License (ODbL) v1.0 (https://opendatacommons.org/licenses/odbl/1-0/)
- **Size:** 918 patients and 12 columns: 11 patient measurements plus the target, `HeartDisease`
- **Origin:** five datasets combined (Cleveland, Hungarian, Switzerland, Long Beach VA, Stalog), 1190 observations, 272 duplicates removed, leaving 918.
- **Target:** `HeartDisease` is a column with two values, 0 and 1.  0 refers to patients without heart disease and 1 refers to patients with heart disease.
- **Cleaning:** The dataset did not require extensive cleaning.  However, `Cholesterol` contained 172 missing values as zeros, which were replaced with the median of the real readings.  This was better than deleting the affected rows which would have removed a significant portion of the dataset; 172 of 918 rows is about 19% of the data.  RestingBP had a single missing value as zero.  This was also replaced with that column's median (130).  No rows were removed. One column, Cholesterol_Missing, was added to mark filled values, so the cleaned data has 918 rows and 13 columns.
- **Raw data:** The raw data has been kept untouched in data/raw/heart.csv.
- **Citation:** fedesoriano (September 2021) Heart Failure Prediction Dataset. Retrieved 07 October 2026 from https://www.kaggle.com/fedesoriano/heart-failure-prediction.

- **Attribution notice:** Contains information from [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/), which is made available here under the [Open Data Commons Open Database License (ODbL) v1.0](https://opendatacommons.org/licenses/odbl/1-0/)


## Hypothesis

- **Null hypothesis (H0):** the average maximum heart rate is the same in both groups.
- **Alternative hypothesis (H1):** the average maximum heart rate is different between the groups, in either direction.
- **Significance level (α):** 0.05, chosen before the test
- **Test:** Welch's t-test, two-tailed. It does not assume that the spread of results is the same in each group.

**Result:** The mean maximum heart rate was 127.7 beats per minute for patients with heart disease (n = 508) and 148.2 beats per minute for those without (n = 410), a gap of about 20.5 beats per minute. The t-statistic was -13.2 and the p-value was <0.001.  The negative sign for the t-statistic is because the heart disease group, listed first in the test, had the lower mean.

**Conclusion:** Because p < 0.001 was below the α of 0.05, I rejected the null hypothesis.  This suggests the two groups differ in their maximum heart rate on exercise, and the heart disease group's mean was lower. This shows an association, not that heart disease causes the lower rate.  Other factors such as age, medication or fitness level might explain the gap.

The full test is in `02_eda.ipynb`, and the box plot in the app shows the difference.

## Credits

- **Creators:**
  - Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
  - University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
  - University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
  - V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
- **Donor:** David W. Aha

## Limitations

