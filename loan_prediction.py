# Importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv(r"C:\Users\a\Downloads\Data1\sales.csv")

# First 5 rows
print("\nFirst 5 Rows")
print(data.head())

# Shape of dataset
print("\nDataset Shape")
print(data.shape)

# Statistical summary
print("\nStatistical Summary")
print(data.describe())

# ================= DATA CLEANING =================

print("\n---------------- Data Cleaning ----------------")

# Missing values
print("\nMissing Values Before Cleaning")
print(data.isnull().sum())

# Remove missing values
data = data.dropna()

print("\nMissing Values After Cleaning")
print(data.isnull().sum())

# Convert Loan_Status into numeric values
if "Loan_Status" in data.columns:
    data["Loan_Status"] = data["Loan_Status"].map({"Y": 1, "N": 0})

# Convert Dependents column
if "Dependents" in data.columns:
    data["Dependents"] = data["Dependents"].replace("3+", 4)
    data["Dependents"] = pd.to_numeric(data["Dependents"])

# ================= DATA VISUALIZATION =================

print("\n---------------- Data Visualization ----------------")

if "Education" in data.columns and "Loan_Status" in data.columns:
    sns.countplot(x="Education", hue="Loan_Status", data=data)
    plt.show()

if "Married" in data.columns and "Loan_Status" in data.columns:
    sns.countplot(x="Married", hue="Loan_Status", data=data)
    plt.show()

# ================= DATA CONVERSION =================

print("\n---------------- Data Conversion ----------------")

data.replace({
    "Married": {"No": 0, "Yes": 1},
    "Gender": {"Male": 1, "Female": 0},
    "Self_Employed": {"No": 0, "Yes": 1},
    "Property_Area": {"Rural": 0, "Semiurban": 1, "Urban": 2},
    "Education": {"Graduate": 1, "Not Graduate": 0}
}, inplace=True)

# Convert all remaining object columns to numeric if possible
for col in data.columns:
    if data[col].dtype == "object" and col != "Loan_ID":
        data[col] = pd.factorize(data[col])[0]

print(data.head())

# ================= DATA SEPARATION =================

print("\n---------------- Data Separation ----------------")

X = data.drop(columns=["Loan_ID", "Loan_Status"])
Y = data["Loan_Status"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", Y.shape)

print("\nTarget Unique Values:")
print(Y.unique())

# ================= DATA SPLITTING =================

print("\n---------------- Data Splitting ----------------")

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.1,
    stratify=Y,
    random_state=2
)

print(X.shape, X_train.shape, X_test.shape)
print(Y.shape, Y_train.shape, Y_test.shape)

# ================= MODEL TRAINING =================

print("\n---------------- Model Training ----------------")
print("\nChecking data before training...")

print("X_train shape:", X_train.shape)
print("Y_train shape:", Y_train.shape)

print("\nX_train data types:")
print(X_train.dtypes)

print("\nY_train data type:")
print(Y_train.dtype)

print("\nUnique values in Y_train:")
print(Y_train.unique())

print("\nMissing values in X_train:")
print(X_train.isnull().sum())

print("\nMissing values in Y_train:")
print(Y_train.isnull().sum())
classifier = svm.SVC(kernel="linear")
print("Starting training...")
classifier.fit(X_train, Y_train)
print("Model Trained Successfully")

# ================= MODEL EVALUATION =================

train_prediction = classifier.predict(X_train)
train_accuracy = accuracy_score(Y_train, train_prediction)

print("\nTraining Accuracy:", train_accuracy)

test_prediction = classifier.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_prediction)

print("Testing Accuracy:", test_accuracy)