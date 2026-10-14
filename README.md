# Heart Failure Analysis

## Overview

This project takes data from studies of 918 patients with and without a heart disease diagnosis, and uses it to investigate differences between patient groups with respect to heart disease diagnosis and maximal heart rate on exercise.  Two machine learning models were used: logistic regression to classify heart disease, and linear regression to predict maximum heart rate.

The project might be useful to beginner data analysts who want to see how to analyse group averages with a t-test, as detailed in the notebooks, and to visualise data in Streamlit with a boxplot and a histogram, as shown in the app.  The project shows how to incorporate a slider into the workflow to make a chart interactive.

The Streamlit app contains a data table showing the first five rows of patient data, an interactive histogram and a boxplot.  The histogram lets the user interact with it by limiting the upper and lower age bounds of the patients in the histogram using a slider widget.

## Live Dashboard

🔗 [View the deployed Streamlit app](https://heart-failure-analysis.onrender.com)

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

## Methods and Justification

**Welch's t-test.** I wanted to know whether the average maximum heart rate differs between patients with and without heart disease. MaxHR is a numeric measurement and there are two independent groups, so comparing their means with a t-test is appropriate.  A t-test gives a p-value, which measures how likely a difference this large would be if both groups really came from the same population, so it goes beyond judging the box plots by eye. I used Welch’s version because it does not assume the two groups have equal spread.

Alternatives include Student’s t-test, which assumes equal spread, and the Mann-Whitney U test, which does not assume the data are normally distributed. With 508 and 410 patients in the groups, the t-test is a reasonable choice.

**Logistic regression (classifying heart disease).** `HeartDisease` is a category (0 or 1). Logistic regression is designed for this: its S-shaped curve keeps every prediction between 0 and 1, so the output can be read as the probability of heart disease. Values above 0.5 are classified as heart disease and values below as no heart disease. A straight-line model could predict values below 0 or above 1, which have no meaning for a yes/no outcome.

A decision tree or random forest could also classify heart disease and may capture more complex patterns, but logistic regression is simpler to interpret and gives probabilities, which suited a learning project.

**Linear regression (predicting maximum heart rate).** `MaxHR` is a number on a scale, which linear regression is designed to predict. It is simple and easy to interpret, and it gives a clear baseline to compare against.

The modest R² suggests the relationships may not be purely linear, so a tree-based model is an alternative I did not try.

## Project Plan

The original plan is in `docs/kanban_plan.md`. Progress was tracked on the [GitHub Project board](https://github.com/users/ImaginationDeadImagine/projects/8/views/1).

**Changes to the plan**

- **Clustering was dropped:** To protect time for the write-up and for checking the finished project, clustering was dropped.  Classification and regression already covered the machine learning requirement. With more time, I would have used k-means (with the features scaled first) to look for clusters within the heart disease patients, and then compared those clusters with the `RestingECG` categories.
- **Extra app pages were dropped:** Hypothesis and Predict pages were dropped.  Again, this was to protect time for the write-up and for checking the finished project.  The final app is a single page.
- **Deployment moved from Heroku to Render:** The Heroku student credits step failed at account activation, so I deployed to Render, which the tutor confirmed was acceptable.

## Ethics and Use of AI

**Privacy:** The dataset contains no direct identifiers such as names or hospital numbers, and it is a public release under the ODbL licence. The remaining columns (for example age, sex and resting ECG) describe measurements, not identities. The raw file is kept unchanged in `data/raw/`.

**Use of AI:** I used Claude (Anthropic) throughout the project as a tutor. It explained concepts, helped plan the work from the assessment handbook, reviewed my wording and helped me find errors in my code and writing. For code, Claude gave worked examples using other columns or tables as patterns, and I wrote, adapted, ran and tested the code for this project's data. Some README wording was drafted or revised with Claude, and I edited it and checked every figure against my notebooks. The analysis choices, the results and the final text are my responsibility.

**Cautions:** This project is a learning exercise and not a diagnostic tool. The results show associations in one pooled dataset and should not be used for clinical decisions.

## Dashboard Design and Deployment

**Design.** The app is a single Streamlit page that follows the project's question: how does maximum heart rate relate to heart disease? It contains:

- a data table showing the first five rows, so users can see what the data looks like
- an interactive histogram with an age slider, so users can explore how the age range changes the picture
- a box plot of maximum heart rate by heart disease category, which shows the difference tested in the hypothesis test
- an attribution notice for the dataset licence

**Deployment.** The app is deployed on Render's free tier from this repository. Render installs the packages listed in `requirements.txt` and starts the app with:

`streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`

I first tried Heroku, but its student credits step failed at account activation, so the Heroku files in the repository (`Procfile`, `setup.sh`, `.slugignore`) are not used by the Render deployment. The `pyarrow` version is pinned in `requirements.txt` for compatibility with NumPy 1.26.

**Libraries.** pandas and NumPy (data handling), matplotlib and seaborn (charts), SciPy (t-test), scikit-learn (logistic and linear regression), Streamlit (the app), and pyarrow (pinned for compatibility).

## Reflection

**Challenges:**
I was initially going to deploy on Heroku as recommended by Code Institute but fell at the last hurdle.  Heroku accepted that I was on the GitHub Student Developer Pack but failed to add credits to my registered account.

I researched other alternatives and selected [Render](https://www.render.com) because it had a free tier.  I checked with a tutor that deploying on Render was acceptable and proceeded with deployment.  For the most part this was straightforward.  Render linked to GitHub and could access my repo, but I had to rely on Claude to build the command that starts the app.  Render's logs showed a NumPy/pyarrow version clash which I fixed by pinning a compatible version.

Statistics concepts (t-test, p-value, R², recall) were very difficult for me to grasp.  I had done statistics involving these concepts in the distant past but, rather than this being a refresher, I was once again pitted against my ignorance and confusion.  Claude prodded and poked me time after time to put explanations of concepts in my own words until they were acceptable, but I think my foundations are quite shaky and require a lot more work.  By the end I had a clearer picture of my limitations (the concepts are still hazy) and of where to concentrate my further learning. What did change is that I could explain the t-test, p-value, R² and recall with support well enough to use them in the Hypothesis, Methods and Limitations sections.

Working in the terminal was confusing, particularly developing a disciplined approach to making commits.  Claude helped by suggesting it was time to commit after a block of work.  Working with git was daunting at first but became mechanical the more I did it.

**New tools:** I used a number of tools and techniques that I had not used before, such as Streamlit, Render and git commits tied to issues on the Kanban board.  For Streamlit I familiarised myself with basic usage with YouTube videos.  Render was fairly straightforward to set up because of its linkage to GitHub.  The Kanban board became a source of comfort as tasks were finished and moved to Done.

**Future work:** I will be more confident about using a progress log as a record of work completed and issues encountered, along with where I might require help or am stuck.

I will investigate using Streamlit more.  I enjoyed how easy it was to get an app up and running.  I will investigate its limitations though, as I understand it has limits for production use, so I will investigate where it suits and where it does not.

I will focus some of my learning on statistical foundations and sharpen my understanding of basic concepts.  I am sure it will find broad applicability in analysing datasets in the future.

I have learned that working with AI is a powerful production technique.  I feel that the project would have been impossible without it in the time available.  I also feel I have only just scratched the surface of its capabilities.  I will look into this further too.

## Limitations

Of the 918 patients in the dataset, 734 were assigned to the training set and 184 to the test set.  A test set of 184 patients is small.

**Classification:** The logistic regression model achieved an accuracy of 0.891 and a recall of 0.922 on a single held-out test set of 184 patients. A different split could give somewhat different scores, so these figures are estimates, not guarantees. A recall of 0.922 also means roughly 8 in 100 patients with heart disease would be missed, which matters in a medical setting. Cross-validation would give a more reliable estimate and is a possible improvement.

**Regression:** On the test set the regression model had an $R^2$ ≈ 0.31. This means the model explains about 31% of the variation in measured maximum heart rate.  This leaves about 69% of the variation not captured by the model.

The MAE is 16.6 beats per minute (bpm) which is the average gap between predicted and measured maximum heart rate (`MaxHR`).  The baseline is 21.4 bpm from predicting the same average for everyone.  All figures are test-set figures.  Although the model improves on the baseline, with a fall of about 22%, it is arguably not a large improvement.

**Pooled hospitals:** The dataset was compiled from studies carried out at several hospitals in different countries.  When the model meets a patient from a hospital or population it has never seen, it may perform less well.  The training data is limited in extent and may not transfer to standard hospitals versus those carrying out research (which may be better resourced 'tertiary' hospitals).  The incidence and severity of heart disease may also vary across regions, and by population demographics such as socioeconomic class.  There is no column in the dataset marking the patients from different hospitals, so it is not possible to check whether the model performs better at some hospitals than others.

## Credits

- **Creators:**
  - Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
  - University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
  - University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
  - V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
- **Donor:** David W. Aha

