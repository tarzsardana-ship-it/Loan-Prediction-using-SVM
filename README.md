# 🏦 Loan Prediction System

A Machine Learning web application that predicts whether a loan application is likely to be approved or rejected based on applicant and financial information.

## 🚀 Live Demo

**Streamlit App:**
https://loan-prediction-using-svm-zuteakuschyvmm3a5fvelh.streamlit.app/

## 📂 GitHub Repository

**Repository:**
https://github.com/tarzsardana-ship-it/Loan-Prediction-using-SVM

---

## 📌 Project Overview

Financial institutions receive a large number of loan applications every day. Manually evaluating every application can be time-consuming and prone to inconsistencies.
This project uses a **Support Vector Machine (SVM)** classification model to analyze applicant details and predict loan approval status.
The application provides an interactive web interface built using **Streamlit**, allowing users to enter applicant information and receive instant predictions.

---

## 🎯 Features

* Loan approval prediction using Machine Learning
* Support Vector Machine (SVM) classifier
* Interactive Streamlit web application
* Data preprocessing and cleaning
* Feature encoding and transformation
* Real-time prediction system
* User-friendly dashboard interface

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

---

## 📊 Dataset Features

The model uses the following input features:

| Feature           | Description               |
| ----------------- | ------------------------- |
| Gender            | Applicant Gender          |
| Married           | Marital Status            |
| Dependents        | Number of Dependents      |
| Education         | Educational Qualification |
| Self_Employed     | Employment Status         |
| ApplicantIncome   | Applicant Income          |
| CoapplicantIncome | Co-applicant Income       |
| LoanAmount        | Loan Amount Requested     |
| Loan_Amount_Term  | Loan Repayment Term       |
| Credit_History    | Credit History Status     |
| Property_Area     | Rural / Semiurban / Urban |

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:
* Removed missing values
* Converted Loan_Status into numerical values
* Encoded categorical variables
* Converted Dependents column into numerical format
* Feature transformation and cleaning
* Dataset preparation for model training

---

## 📈 Model Performance

| Metric            | Score  |
| ----------------- | ------ |
| Training Accuracy | 78.94% |
| Testing Accuracy  | 83.33% |

The model demonstrates good generalization performance on unseen data.

---

## 🖥️ Streamlit Application
The web application allows users to:
1. Enter applicant details
2. Provide financial information
3. Predict loan approval status instantly
4. Receive approval/rejection results in real time

---

## ▶️ Run Locally
### Clone Repository
git clone https://github.com/tarzsardana-ship-it/Loan-Prediction-Using-SVM.git
### Move into Project Directory
cd Loan-Prediction-Using-SVM
### Install Dependencies
pip install -r requirements.txt 
### Run Streamlit App - streamlit run app.py
---

## 📷 Application Preview
Smart Loan Approval Prediction System
* Applicant Information Section
* Financial Information Section
* Instant Prediction Output
* Clean Dashboard Interface

---

## ⭐ Future Improvements

* Probability Score Prediction
* Loan Eligibility Analytics Dashboard
* Feature Importance Visualization
* Advanced Model Comparison
* Cloud Database Integration

