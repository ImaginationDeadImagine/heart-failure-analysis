# Capstone Assessment 2: Progress Log

## Wednesday 14 October

**Done**
- Pinned `pyarrow` to fix the NumPy clash on Render; the app is now live on Render (#19)
- Removed the duplicate box plot title from the app
- Added the live app link to the README
- Completed the README: Project Plan, Methods and Justification (with alternatives), Ethics and Use of AI, Dashboard Design and Deployment, Limitations, Reflection

**Next**
- Submit the project
- Remove the duplicate Project Plan heading in the README
- Add a core statistics concepts section to the EDA notebook (mean, median, standard deviation, basic probability) if time allows

**Stuck or unsure**
- Notebook may only partly meet criterion 1.1 (basic probability and how the principles are foundational to data analysis)
- Statistics foundations are still hazy and need more practice
- Whether publishing the data files needs any further ODbL steps

## Tuesday 13 October (afternoon/evening)

- Done

  - Tutor confirmed a Streamlit dashboard must be deployed. Checked the template’s deployment files (.slugignore, .python-version, Procfile, setup.sh): all suitable.
  - Trimmed requirements.txt to the 7 packages the project uses; removed unused ones (ydata-profiling, ppscore, yellowbrick, Pillow, plotly, imbalanced-learn, xgboost, feature-engine). Added scipy==1.13.1, which notebook 02 uses directly.
  - GitHub Student Developer Pack granted. Applied for Heroku student access.
  - Replaced the template README with a project overview, Dataset section (source, ODbL licence, origin, cleaning of 172 Cholesterol zeros and 1 RestingBP zero) and Credits. Fixed formatting after review.
  - Added the ODbL attribution notice to the app (st.caption) and the README.
  - All committed and pushed; working tree clean.

- Next

  - Deploy to Heroku once access arrives; add the live link to the README.
  - Remaining README sections: hypothesis, project plan, analysis techniques, ethics, dashboard design, limitations, libraries, sources and help.
  - Reflection (#16) and final handbook check (#17). Submit by lunchtime Wed.

- Stuck or unsure

  - Heroku access pending. If it hasn’t arrived by the morning, the fallback is Render (the tutor says any platform is acceptable).
  - Unsure whether publishing the data files in a public repo needs further ODbL steps. May ask the tutor.
  - Dropped the extra app pages (hypothesis test, Predict) to protect time for the required deployment and write-up.

## Tuesday 13 Oct (morning)

- Done:
  - Terminal froze after overnight sleep. Fixed by deleting old terminals and opening a new one, which showed (.venv). Confirmed with git status: working tree clean.
  - Ran the Streamlit app to check it still worked: table, age histogram and slider all fine.
  - Added a box plot of MaxHR by heart disease status to app.py. First attempt failed (AttributeError) because I put seaborn arguments into plt.subplots(). Fixed by using plt.subplots() to make the canvas and sns.boxplot() to draw on it.
  - Found a copy-paste error: the y-axis label said “Number of patients” when it shows MaxHR. Corrected it.
  - Result: patients without heart disease reach higher maximum heart rates. The median line of box 0 sits above the top edge of box 1, consistent with the t-test.
  - Committed and pushed (#14).
- Next:
  - Move card #14 to Done on the kanban board.
  - Write the README (#15), one section at a time.
  - Then, if time and energy allow: hypothesis test page in the app. Predict page is optional.
  - Reflection (#16) and final handbook check (#17) before submitting on Wednesday.
- Stuck or unsure:
  - First box plot attempt failed with AttributeError: Figure.set() got an unexpected keyword argument 'data'. I had put the seaborn arguments inside plt.subplots(). Fixed by using plt.subplots() for the canvas and sns.boxplot() to draw on it.
  - Copied the histogram’s y-axis label (“Number of patients”) onto the box plot by mistake. Spotted it on review and corrected it.
  - Unsure how many app pages to build before the deadline. I want to do the required README first, then decide.

## Monday 12 October (evening)
- Done:
  - Created a Streamlit app (app.py) with a title, a data table, an age histogram and an age slider that filters the chart (#14)
  - Committed each step as a small commit
- Next:
  - Add a hypothesis test page and a Predict page (save the classification model to a file first)
  - README (#15)
- Stuck or unsure:
  - VS Code autocomplete changed a line of code; fixed by pressing Esc before Enter
  - Chart ignored the slider until it used the filtered data instead of the full data

## Monday 12 October
- Done:
  - Finished regression: predicted MaxHR with linear regression (R-squared 0.31, average error 16.6 bpm against 21.4 for an always-the-average baseline) and wrote it up (#12)
  - Committed and moved card #12 to Done
- Next:
  - Streamlit app (#14)
  - README (#15), reflection (#16), then the final check against the handbook (#17)
- Stuck or unsure:
  - Working directory error after a restart, fixed by running the directory cells once each
  - A variable accidentally overwrote the mean_absolute_error function; fixed by using different names for results

## Sunday 11 October
- Done:
  - Finished classification: split the data into training and test sets, trained a logistic regression model, and evaluated it (accuracy 89%, recall 92%, precision 89%) (#11)
  - Wrote up the results, including the confusion matrix, the baseline comparison and the caveats, then committed and moved card #11 to Done
  - Set up 04_regression.ipynb to predict MaxHR, loaded the cleaned data (918 rows, 13 columns) and committed the skeleton (#12)
- Next:
  - Separate features and target for regression (MaxHR is the target, so it is dropped from X; HeartDisease may stay in as a feature)
  - Encode the text columns, split into training and test sets, then fit a linear regression and judge it
- Stuck or unsure:
  - The roles of features and target switch between notebooks (HeartDisease was the target in classification, MaxHR is the target in regression)
  - Needed several rounds to get the results write-up accurate

## Saturday 10 / Sunday 11 October (late evening)
- Done:
  - Set up 03_classification.ipynb (header, kernel, directory cells, imports, data load) and committed the skeleton (#11)
  - Separated the features (X) from the target (y), keeping HeartDisease out of X
  - One-hot encoded the text features into X_encoded, dropping one category per column
  - Committed a small edit to the 02_eda notebook title
- Next:
  - Split the data into training and test sets
  - Train a simple classification model (probably logistic regression) and evaluate it, focusing on recall
- Stuck or unsure:
  - Template notebook kept showing as modified in Git, so I checked what changed before committing
  - Nearly encoded df instead of X, which would have leaked the target into the features

## Saturday 10 October
- Done:
  - Split MaxHR into patients with and without heart disease (508 and 410; means 127.7 and 148.2)
  - Ran Welch's two-tailed t-test (t = -13.2, p < 0.001), rejected H0 and wrote up the result
  - Hypothesis test (#10) committed and cards moved on the board
- Next:
  - Set up 03_classification.ipynb and load the cleaned data (#11)
  - Encode the text columns, then train and evaluate a model
- Stuck or unsure:
  - VS Code needed complete shut down and restart to clear hang in Extensions panel following Extensions restart
  - Restarting the kernel clears the working directory, so the directory cells must be re-run in order, once each
  - Terminal git commit command doubled up by mistake.

## Friday 9 October
- Done:
  - Saved cleaned data to data/processed (#8) and added the encoding note
  - Built EDA charts: age histogram, heart disease count plot and MaxHR box plot (#9)
  - Wrote statistics definitions and the hypotheses (two-tailed, alpha 0.05) (#10)
- Next:
  - Split MaxHR into two groups and run the t-test
- Stuck or unsure:
  - Wording of the statistics definitions took several rounds
  - Directory cell run twice, fixed by restarting the kernel

## Wednesday 7/Thursday 8 October
- Done:
  - Completion of ETL.  Encoding of text columns postponed:
    - so data labels can be used in EDA charts
    - as different models encode in different ways
    - so the ETL stages show cleaning only
- Next:
  - Begin with encoding in modelling notebooks
  - EDA plots and the hypothesis test
- Stuck or unsure:
    - The template’s directory cell was run twice (my tremor!).
    - Decided what to do with the zero values (fill or drop?  Fill).
    - Template notebook shows as modified several times, restored with git restore.

## Tuesday 6 October
- Done:
  - Repo template cloned to `C:\Code Institute - Data Analytics\heart-failure-analysis`
  - Virtual environment created using Python 3.12.8, along with matching notebook kernel
  - All libraries installed (following fix for ppscore using setuptools<81)
  - docs/kanban_plan.md committed
  - Kanban board issues #6 to #17 outstanding, with #6 in progress
  - Data placed in data/raw/heart.csv and pushed
- Next:
  - Plan to complete extract, transform and load (issues #6, #7 and #8)
- Stuck or unsure:
  - Python 3.14.6 installed, but 3.12.8 needed.  Sorted correct kernel version.
  - ppscore failed to install, fixed with setuptools<81.
  - First clone came from the original template, not my own copy.
