# 🏦 Customer Churn Analysis using Machine Learning & Power BI

> **End-to-End Customer Churn Analysis** using Python, Machine Learning, and Power BI.

---

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

| Aspect | Details |
|--------|---------|
| **Dataset** | Bank Customer Churn Dataset |
| **Total Records** | 10,000 |
| **Features** | 12 |
| **Target Variable** | Churn (0 = Stayed, 1 = Churned) |

### Features Description

| Column | Description |
|--------|-------------|
| `customer_id` | Unique customer ID |
| `credit_score` | Customer credit score |
| `country` | Country of residence (France, Germany, Spain) |
| `gender` | Gender (Male, Female) |
| `age` | Customer age |
| `tenure` | Years with the bank |
| `balance` | Account balance |
| `products_number` | Number of products used |
| `credit_card` | Has credit card? (0 = No, 1 = Yes) |
| `active_member` | Is active member? (0 = No, 1 = Yes) |
| `estimated_salary` | Estimated annual salary |
| `churn` | **Target:** 0 = Stayed, 1 = Churned |

---

## 📊 Key Findings

- **Churn Rate**: 20.37% customers churned
- **Highest Risk Market**: Germany (32.44% churn rate)
- **Inactive Members**: 2x more likely to churn (26.85% vs 14.27%)
- **Age Factor**: Customers above 50 show 45%+ churn rate
- **High Balance**: Customers with >₹1L balance are more likely to churn
- **Female Customers**: Higher churn rate (25.07% vs 16.46%)

---

## 💡 Business Recommendations

1. **🇩🇪 Germany Focus**: Launch Germany-specific retention campaigns
2. **👴 Senior Citizens**: Create senior citizen banking packages
3. **📱 Inactive Members**: Re-engagement campaigns for inactive customers
4. **💎 High Balance**: Premium services for high-balance customers
5. **👩 Female Customers**: Targeted engagement programs for female customers

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Python** | Data processing, EDA, Machine Learning |
| **Pandas & NumPy** | Data manipulation |
| **Matplotlib & Seaborn** | Data visualization |
| **Scikit-learn** | Machine Learning models |
| **Joblib** | Model serialization |
| **Jupyter Notebook** | Interactive development |
| **Power BI** | Dashboard & Business Intelligence |

---

## 📈 Exploratory Data Analysis (EDA)

### Univariate Analysis
- Customer Churn Distribution
- Gender Distribution
- Country Distribution
- Age Distribution

### Bivariate Analysis
- Gender vs Churn
- Country vs Churn
- Active Member vs Churn
- Balance vs Churn
- Age vs Churn
- Products vs Churn

### Correlation Analysis
- Correlation Heatmap of all numerical features

### Key EDA Insights
- France has largest customer base but Germany has highest churn
- Inactive members show significantly higher churn rates
- Age has strongest correlation with churn (0.29)
- Active Member has strongest negative correlation (-0.16)

---

## 🤖 Machine Learning Models

Three models were trained and evaluated:

### 1. Logistic Regression
- Simple, interpretable baseline model
- Good for understanding feature impact

### 2. Decision Tree Classifier
- Non-linear decision boundaries
- More interpretable than ensemble methods

### 3. Random Forest Classifier
- Ensemble of decision trees
- Reduces overfitting
- Better generalization

---

## 📊 Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 80.80% | 0.59 | 0.19 | 0.28 |
| Decision Tree | 78.25% | 0.47 | 0.51 | 0.49 |
| **Random Forest** | **86.40%** | **0.78** | **0.46** | **0.58** |

### 🏆 Best Model: Random Forest

**Why Random Forest?**
- ✅ Highest Accuracy (86.40%)
- ✅ Highest Precision (0.78)
- ✅ Highest F1-Score (0.58)
- ✅ Most balanced performance
- ✅ Handles non-linear relationships well

### Confusion Matrix - Random Forest

```
Actual vs Predicted:
            Predicted
            No    Yes
Actual  No  1541   52
        Yes  220  187
```

- **True Negatives**: 1,541 (Correctly predicted non-churn)
- **False Positives**: 52 (Incorrectly predicted churn)
- **False Negatives**: 220 (Missed churn customers)
- **True Positives**: 187 (Correctly predicted churn)

---

## 🔍 Feature Importance (Random Forest)

| Feature | Importance |
|---------|-----------|
| **Age** | 23.65% |
| **Estimated Salary** | 14.70% |
| **Credit Score** | 14.28% |
| **Balance** | 14.18% |
| **Products Number** | 13.04% |
| **Tenure** | 8.18% |
| **Active Member** | 3.99% |
| **Country_Germany** | 2.89% |
| **Credit Card** | 1.88% |
| **Gender_Male** | 1.85% |
| **Country_Spain** | 1.36% |

---

## 📊 Power BI Dashboard

### Dashboard Components

| Component | Description |
|-----------|-------------|
| **KPI Cards** | Total Customers, Active Customers, Churn Customers, Churn Rate, Average Balance |
| **Country-wise Churn** | Bar chart showing churn distribution by country |
| **Gender-wise Churn** | Bar chart showing churn by gender |
| **Products vs Churn** | Bar chart showing churn by number of products |
| **Active Members vs Churn** | Bar chart showing churn by active status |
| **Age Distribution** | Histogram showing customer age distribution |

### Interactive Slicers
- 🌍 **Country**: France, Germany, Spain
- 👤 **Gender**: Male, Female
- 🔄 **Customer Status**: Active, Inactive

### Dashboard Preview

![Dashboard](../Image/imagesdashboard.png)

---

## 📁 Project Structure

```
Customer-Churn-Analysis/
│
├── 📁 Data Set/
│   └── Bank_Customer_Churn_Prediction.csv
│
├── 📁 Notebooks/
│   └── 01_Data_Loading.ipynb
│
├── 📁 Dashboard/
│   └── Customer_Churn_Dashboard.pbix
│
├── 📁 Models/
│   └── customer_churn_model.pkl
│
├── 📁 Image/
│   └── dashboard.png
│
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 LICENSE
```

---

## 🚀 How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/ShubhamKatiyar780/Customer-Churn-Analysis.git
cd Customer-Churn-Analysis
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Jupyter Notebook

```bash
jupyter notebook Notebooks/01_Data_Loading.ipynb
```

### Step 4: Open Power BI Dashboard

1. Open `Dashboard/Customer_Churn_Dashboard.pbix`
2. Refresh the data source
3. Interact with slicers and visuals

---

## 🔮 Future Improvements

| Area | Improvement |
|------|-------------|
| **Hyperparameter Tuning** | GridSearchCV for optimal parameters |
| **Advanced Models** | XGBoost, LightGBM, Neural Networks |
| **Imbalance Handling** | SMOTE, class weights |
| **Model Explainability** | SHAP, LIME for interpretability |
| **Deployment** | Streamlit or Flask web app |
| **Real-time Monitoring** | MLflow for model tracking |
| **Data Enrichment** | Add more customer behavior features |

---

## 📝 Conclusion

The Customer Churn Analysis project successfully:

✅ Identified key factors driving customer churn
✅ Built a Random Forest model with **86.40% accuracy**
✅ Created an interactive Power BI dashboard
✅ Provided actionable business recommendations

**Key Takeaway**: Customer age, activity status, and country of residence are the strongest predictors of churn. Banks should focus their retention efforts on high-risk segments identified through this analysis.

---

## 👨‍💻 Author

**Mr. Shubham Katiyar**

Data Analytics | Machine Learning | Power BI

📧 Email: [shubhamkatiyar780@gmail.com](mailto:shubhamkatiyar780@gmail.com)

🔗 LinkedIn: [linkedin.com/in/shubhamkatiyar780](https://linkedin.com/in/shubhamkatiyar780)

🐙 GitHub: [github.com/ShubhamKatiyar780](https://github.com/ShubhamKatiyar780)

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

**Made with ❤️ by Shubham Katiyar**
