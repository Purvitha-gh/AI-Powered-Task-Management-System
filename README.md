# AI-Powered-Task-Management-System
AI-Powered Task Management System

📌 Overview

An AI-Powered Task Management System that leverages NLP and ML to automatically classify tasks, predict priority, and balance workloads. This project was executed in 4 structured weeks, progressing from data preparation to model deployment and performance reporting.

🧠 Problem Statement

Design and develop an intelligent task management system that:

Classifies tasks into categories based on descriptions

Predicts task priority (High, Medium, Low)

Assigns tasks based on user workload and behavior

🗓️ Weekly Breakdown

✅ Week 1: Data Preparation

Collected a synthetic task dataset from Kaggle

Performed data cleaning:

Removed nulls and duplicates

Normalized text

Applied NLP preprocessing:

Tokenization

Stopword removal

Stemming

Conducted EDA:

Category distribution

Word frequency and word cloud

✅ Week 2: Task Classification

Feature extraction with TF-IDF

Built two classifiers:

Multinomial Naive Bayes

Support Vector Machine (SVM)

Evaluation results:

Model

Accuracy

Precision

Recall

F1-Score

Naive Bayes

84%

85%

83%

84%

SVM

88%

89%

87%

88%

Set up GitHub repository for version control

✅ Mid-Project Review

Cleaned & preprocessed dataset available

Trained classification models (NB and SVM)

EDA visualizations documented

✅ Week 3: Priority Prediction + Workload Logic

Built models:

Random Forest

XGBoost

Applied GridSearchCV for hyperparameter tuning

Evaluation results:

Model

Accuracy

Precision

Recall

F1-Score

Random Forest

81%

82%

80%

81%

XGBoost

85%

84%

86%

85%

Implemented workload balancing using heuristic logic:

Assign tasks to the user with the least current workload

✅ Week 4: Finalization

Final Models:

Task Classification: SVM

Priority Prediction: XGBoost

Created output summaries & mock dashboard views

Sample output table:

Task

Category

Priority

Fix production bug

Development

High

Update documentation

Documentation

Medium

Schedule team call

Management

Low

📊 Final Metrics Summary

Task

Model

Accuracy

Precision

Recall

F1-Score

Task Classification

SVM

88%

89%

87%

88%

Priority Prediction

XGBoost

85%

84%

86%

85%

🔮 Future Scope

Use contextual word embeddings like BERT

Automate user workload tracking via dashboards

Integration with calendar APIs (Google/Outlook)

Real-time task routing engine

📁 Project Structure

├── data/                    # Raw & processed datasets
├── notebooks/               # EDA, training, evaluation
├── models/                  # Trained model binaries
├── scripts/                 # Helper and utility scripts
├── visualizations/          # Charts, graphs, confusion matrices
└── README.md                # Project overview


✅ Conclusion

This project demonstrates a practical application of NLP and ML to automate task classification, prioritization, and workload balancing. With high-performing models and intuitive logic, it lays the foundation for enterprise-ready task management automation.
