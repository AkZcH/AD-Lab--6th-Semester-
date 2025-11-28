# 🧹 Data Preprocessing & Exploratory Data Analysis (EDA)

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A structured workflow demonstrating **data preprocessing** and **exploratory data analysis (EDA)** using standard ML preparation techniques and the **Iris dataset**.

---

## 📁 Table of Contents
- [Overview](#overview)
- [Data Preprocessing](#data-preprocessing)
  - [Handling Missing Values](#handling-missing-values)
  - [Encoding Categorical Data](#encoding-categorical-data)
  - [Feature Scaling](#feature-scaling)
- [Dataset Description](#dataset-description)
- [Exploratory Data Analysis](#exploratory-data-analysis)
  - [Histogram](#histogram)
  - [Scatter Plot](#scatter-plot)
  - [Correlation Heatmap](#correlation-heatmap)
- [Summary](#summary)
- [License](#license)

---

## 🔍 Overview

The project showcases a complete end-to-end preprocessing pipeline combined with fundamental visual EDA. It focuses on preparing real-world structured data for machine learning workflows and demonstrating feature relationships using the Iris dataset.

---

## 🛠️ Data Preprocessing

### ✔ Handling Missing Values

#### Numerical Columns (Age, Salary)
- Missing entries are replaced using **mean imputation** via `SimpleImputer(strategy="mean")`.
- This preserves numerical distribution consistency.

#### Categorical Columns (Country)
- Missing values are imputed using the **most frequent category** (`strategy="most_frequent"`).
- Maintains category balance without distortion.

---

### ✔ Encoding Categorical Data

#### Label Encoding
- Categorical fields such as **Gender** and **Country** are transformed to integer labels using **LabelEncoder**.
- Enables seamless model consumption of previously non-numeric data.

---

### ✔ Feature Scaling

#### Standardization
- Numerical features (**Age**, **Salary**) are scaled using **StandardScaler**.
- Transforms the data to:
  - Mean = 0  
  - Standard deviation = 1  
- Improves model stability and comparability across features.

---

## 🌸 Dataset Description

The **Iris dataset** is loaded using `sns.load_dataset("iris")`.

It includes 150 samples with:

- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`
- `species`

A widely used benchmark dataset for demonstrating ML preprocessing and EDA workflows.

---

## 📊 Exploratory Data Analysis

### 📈 Histogram
- Visualizes the distribution of **sepal_length**.
- Helps detect skew, central tendency, and anomalies.

---

### 🔵 Scatter Plot
- Explores the relationship between **sepal_length** and **sepal_width**.
- Points are differentiated by **species**, enabling cluster separation analysis.

---

### 🔥 Correlation Heatmap
- Computes correlations across numerical features.
- Heatmap highlights:
  - Strong/weak correlations
  - Linear dependencies
  - Feature redundancy

---

## 🧾 Summary

This project delivers:

- A complete preprocessing pipeline: **imputation, encoding, scaling**
- A structured EDA routine: **distribution, relationships, correlations**
- A clean, interpretable dataset ready for downstream ML tasks

---

## 📄 License

This project is licensed under the **MIT License**.

