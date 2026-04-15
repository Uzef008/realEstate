import streamlit as st
import pickle
import numpy as np
import os
import gdown

# -------------------------------
# Download Models from Google Drive
# -------------------------------

# Google Drive File IDs
CLASSIFIER_ID = "17xv3DEr9WS_uNTpuPpslCaWEd9Hi0Yhs"
REGRESSOR_ID = "1hJ_xA1pEVSYW3iuqYAKJCPv1X5TsDu6X"

def download_model(file_id, output):
    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)

# Download models
download_model(CLASSIFIER_ID, "classifier.pkl")
download_model(REGRESSOR_ID, "regressor.pkl")

# -------------------------------
# Load Models
# -------------------------------

with open("classifier.pkl", "rb") as f:
    clf = pickle.load(f)

with open("regressor.pkl", "rb") as f:
    reg = pickle.load(f)

# -------------------------------
# Streamlit UI
# -------------------------------

st.title("Real Estate Investment Advisor")

st.write("Enter property details to get predictions")

# Inputs
bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)
size = st.number_input("Size in SqFt", min_value=100, max_value=10000, value=1000)
price = st.number_input("Price in Lakhs", min_value=1, max_value=1000, value=50)
floor = st.number_input("Floor No", min_value=0, max_value=50, value=1)
total_floors = st.number_input("Total Floors", min_value=1, max_value=100, value=5)
parking = st.number_input("Parking Space", min_value=0, max_value=5, value=1)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict"):
    
    # Create input array (must match training feature order)
    input_data = np.array([[ 
        0, 0, 0, 0,         # Encoded categorical placeholders
        bhk,
        size,
        price,
        price / size,
        2000,               # Year_Built (default)
        0, 0,
        floor,
        total_floors,
        10,                 # Age_of_Property
        2, 2, 1,
        parking,
        1, 1, 1, 1
    ]])

    # Predictions
    prediction_clf = clf.predict(input_data)[0]
    prediction_reg = reg.predict(input_data)[0]

    # Output
    if prediction_clf == 1:
        st.success("Good Investment")
    else:
        st.error("Not a Good Investment")

    st.write(f"Estimated Price after 5 years: {prediction_reg:.2f} Lakhs")
