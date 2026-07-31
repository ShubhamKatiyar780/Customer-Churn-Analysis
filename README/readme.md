# 🏦 Customer Churn Analysis using Machine Learning & Power BI

## 📌 Project Overview

This project focuses on predicting customer churn for a bank using Machine Learning and visualizing business insights with Power BI. The goal is to identify customers who are likely to leave the bank and help businesses take proactive retention actions.

---

## 🎯 Problem Statement

Customer churn is a major challenge for banks as losing customers directly impacts revenue. The objective of this project is to analyze customer behavior, identify key churn factors, and build predictive models that can classify whether a customer is likely to churn.

---

## 🎯 Objectives

- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Identify factors affecting customer churn.
- Build and compare Machine Learning models.
- Visualize insights using Power BI.
- Recommend business strategies to reduce churn.

---

## 📊 Dataset Information

- **Dataset:** Bank Customer Churn Dataset
- **Total Records:** 10,000
- **Features:** 12
- **Target Variable:** Churn

**Target Variable**

- 0 → Customer Stayed
- 1 → Customer Churned

### Features

- Customer ID
- Credit Score
- Country
- Gender
- Age
- Tenure
- Balance
- Products Number
- Credit Card
- Active Member
- Estimated Salary
- Churn

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook
- Power BI

---

## 📈 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Customer Churn Distribution
- Gender Distribution
- Country Distribution
- Age Distribution
- Gender vs Churn
- Country vs Churn
- Active Member vs Churn
- Balance vs Churn
- Age vs Churn
- Products vs Churn
- Correlation Analysis

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|--------|---------:|----------:|--------:|---------:|
| Logistic Regression | 80.80% | 0.59 | 0.19 | 0.28 |
| Decision Tree | 78.25% | 0.47 | 0.51 | 0.49 |
| Random Forest | **86.40%** | **0.78** | **0.46** | **0.58** |

### Best Model

🏆 **Random Forest**

Reasons:

- Highest Accuracy
- Highest Precision
- Highest F1-Score
- Balanced Performance

---

## 📌 Feature Importance

The Random Forest model identified the following as the most influential features:

- Age
- Estimated Salary
- Credit Score
- Balance
- Products Number
- Active Member
- Tenure

---

## 📊 Power BI Dashboard

The dashboard includes:

- KPI Cards
  - Total Customers
  - Active Customers
  - Churn Customers
  - Churn Rate
  - Average Balance

- Country-wise Customer Churn
- Gender-wise Customer Churn
- Products vs Customer Churn
- Active Members vs Customer Churn

Interactive slicers:

- Country
- Gender
- Customer Status

---

## 💡 Key Business Insights

- Germany has the highest customer churn rate.
- Female customers churn more frequently than male customers.
- Inactive customers are more likely to churn.
- Customers with only one product have higher churn.
- Age is the most important predictor of customer churn.
- Random Forest achieved the best overall performance.

---

## 📁 Project Structure

```
Customer-Churn-Analysis/
│
├── data/
│   └── customer_churn.csv
│
├── notebooks/
│   └── Customer_Churn_Analysis.ipynb
│
├── dashboard/
│   └── Customer_Churn_Dashboard.pbix
│
├── models/
│   └── customer_churn_model.pkl
│
├── images/
│   └── dashboard.png
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository.
2. Install the required libraries.

```bash
pip install -r requirements.txt
```

3. Open the Jupyter Notebook.
4. Run all cells.
5. Open the Power BI dashboard (.pbix).

---

## 📷 Dashboard Preview

> Add your Power BI dashboard screenshot here.

```markdown
![Dashboard](images/dashboard.png)
```

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- XGBoost Model
- LightGBM Model
- SHAP Explainability
- Model Deployment using Streamlit or Flask

---

## 👨‍💻 Author

**Mr. Shubham Katiyar**

Data Analytics | Machine Learning | Power BI

---