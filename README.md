# 🏡 Real Estate Investment Advisor

## 📌 Project Overview

The **Real Estate Investment Advisor** is a Machine Learning-based web application that helps users make informed property investment decisions.
It predicts:

* ✅ Whether a property is a **Good Investment** (Classification)
* 💰 The **Estimated Property Price after 5 Years** (Regression)

This project combines **data analysis, machine learning, and web deployment** using Streamlit.

---

## 🎯 Objectives

* Analyze real estate data to identify key factors affecting property prices
* Build a classification model to determine investment potential
* Build a regression model to forecast future property prices
* Deploy an interactive web application for user predictions

---

## 🧠 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib, Seaborn

---

## 📊 Dataset

* Dataset: `india_housing_prices.csv`
* Contains property details such as:

  * Location (State, City, Locality)
  * Property Type, BHK, Size
  * Price and Price per SqFt
  * Amenities, Infrastructure, and Ownership

---

## ⚙️ Project Workflow

### 1. Data Preprocessing

* Handled missing values
* Removed duplicates
* Encoded categorical features
* Feature engineering (Price per SqFt, Age of Property)

### 2. Exploratory Data Analysis (EDA)

* Price distribution analysis
* Location-based trends
* Correlation analysis

### 3. Model Building

#### 🔹 Classification Model

* Target: **Good Investment**
* Algorithm: Random Forest Classifier

#### 🔹 Regression Model

* Target: **Future Price**
* Algorithm: Random Forest Regressor

---

## 📈 Model Evaluation

### Classification:

* Accuracy
* F1-score
* Confusion Matrix

### Regression:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

---

## 🚀 Streamlit Application

The application allows users to:

* Enter property details
* Get prediction:

  * ✔ Good Investment or Not
  * ✔ Estimated Future Price

### ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── classifier.pkl
│   └── regressor.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
└── data/
    └── india_housing_prices.csv
```

---

## 💡 Future Improvements

* Add dropdowns for City, Property Type
* Use advanced models like XGBoost
* Integrate real-time data
* Improve UI/UX design

---

## 📌 Conclusion

This project demonstrates how Machine Learning can be applied to **real-world investment decision-making**.
It provides a practical tool for predicting property value and evaluating investment opportunities.

---

## 🙏 Acknowledgment

This project was developed as part of an internship/academic learning experience to apply Machine Learning concepts in a real-world scenario.
