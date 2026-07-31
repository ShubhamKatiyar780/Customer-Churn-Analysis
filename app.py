# =========================================
# Customer Churn Prediction Web App
# Using Pickle (No joblib dependency)
# =========================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# =========================================
# Page Configuration
# =========================================
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="🏦",
    layout="wide"
)

# =========================================
# Title
# =========================================
st.title("🏦 Customer Churn Prediction App")
st.markdown("### Predict if a bank customer will churn or stay")
st.markdown("---")

# =========================================
# Load Model using Pickle
# =========================================
@st.cache_resource
# Try multiple paths
def load_model():
    possible_paths = [
        "customer_churn_model.pkl",
        "Models/customer_churn_model.pkl",
        "models/customer_churn_model.pkl"
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            with open(path, "rb") as f:
                model = pickle.load(f)
            return model
    
    st.error("❌ Model file not found in any location!")
    return None
    
    # Load model using pickle
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

if model is None:
    st.stop()

# =========================================
# Sidebar - Input Features
# =========================================
st.sidebar.header("📊 Customer Information")

st.sidebar.subheader("👤 Personal Details")
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=35)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
country = st.sidebar.selectbox("Country", ["France", "Germany", "Spain"])

st.sidebar.subheader("💰 Financial Details")
credit_score = st.sidebar.number_input("Credit Score", min_value=300, max_value=850, value=650)
balance = st.sidebar.number_input("Account Balance (₹)", min_value=0, max_value=500000, value=50000)
estimated_salary = st.sidebar.number_input("Estimated Salary (₹)", min_value=10000, max_value=300000, value=60000)

st.sidebar.subheader("🏦 Banking Details")
tenure = st.sidebar.slider("Tenure (Years with Bank)", min_value=0, max_value=10, value=3)
products_number = st.sidebar.selectbox("Number of Products Used", [1, 2, 3, 4])
credit_card = st.sidebar.selectbox("Has Credit Card?", ["No", "Yes"])
active_member = st.sidebar.selectbox("Is Active Member?", ["No", "Yes"])

# =========================================
# Convert Inputs to Model Format
# =========================================
def preprocess_input(age, gender, country, credit_score, balance, 
                     estimated_salary, tenure, products_number, 
                     credit_card, active_member):
    
    # Encode categorical variables
    gender_Male = 1 if gender == "Male" else 0
    country_Germany = 1 if country == "Germany" else 0
    country_Spain = 1 if country == "Spain" else 0
    credit_card_val = 1 if credit_card == "Yes" else 0
    active_member_val = 1 if active_member == "Yes" else 0
    
    # Create feature array (same order as training)
    features = [
        credit_score,        # credit_score
        age,                 # age
        tenure,              # tenure
        balance,             # balance
        products_number,     # products_number
        credit_card_val,     # credit_card
        active_member_val,   # active_member
        estimated_salary,    # estimated_salary
        country_Germany,     # country_Germany
        country_Spain,       # country_Spain
        gender_Male          # gender_Male
    ]
    
    return np.array(features).reshape(1, -1)

# =========================================
# Prediction Section
# =========================================
st.markdown("## 🔍 Prediction Result")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Predict Churn", use_container_width=True):
        
        # Preprocess input
        features = preprocess_input(
            age, gender, country, credit_score, balance,
            estimated_salary, tenure, products_number,
            credit_card, active_member
        )
        
        # Make prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        
        # Display result
        if prediction == 0:
            st.success("✅ **Customer is likely to STAY!**")
            st.metric("Churn Probability", f"{probability*100:.2f}%", delta="Safe")
        else:
            st.error("⚠️ **Customer is likely to CHURN!**")
            st.metric("Churn Probability", f"{probability*100:.2f}%", delta="Risk")
        
        # Show probability meter
        st.progress(float(probability))
        
        # Additional info
        confidence = (1 - abs(probability - 0.5) * 2) * 100
        st.caption(f"Confidence: {confidence:.1f}%")

# =========================================
# Footer
# =========================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 14px;">
    Built with ❤️ using Streamlit | Customer Churn Analysis Project
</div>
""", unsafe_allow_html=True)
