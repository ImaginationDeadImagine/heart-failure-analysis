# Capstone Assessment 2: Progress Log

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
