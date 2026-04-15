import streamlit as st
import pickle
import numpy as np
import os
import requests

# Function to download file from Google Drive
def download_file(url, filename):
    if not os.path.exists(filename):
        r = requests.get(url)
        with open(filename, "wb") as f:
            f.write(r.content)

# Google Drive direct links
classifier_url = "https://drive.google.com/file/d/17xv3DEr9WS_uNTpuPpslCaWEd9Hi0Yhs"
regressor_url = "https://drive.google.com/file/d/1hJ_xA1pEVSYW3iuqYAKJCPv1X5TsDu6X"

# Download models if not present
download_file(classifier_url, "classifier.pkl")
download_file(regressor_url, "regressor.pkl")

# Load models
with open("classifier.pkl", "rb") as f:
    clf = pickle.load(f)

with open("regressor.pkl", "rb") as f:
    reg = pickle.load(f)

st.title("Real Estate Investment Advisor")

st.write("Enter property details to get predictions")

# Inputs
bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)
size = st.number_input("Size in SqFt", min_value=100, max_value=10000, value=1000)
price = st.number_input("Price in Lakhs", min_value=1, max_value=1000, value=50)
floor = st.number_input("Floor No", min_value=0, max_value=50, value=1)
total_floors = st.number_input("Total Floors", min_value=1, max_value=100, value=5)
parking = st.number_input("Parking Space", min_value=0, max_value=5, value=1)

# Dummy feature vector (must match training structure)
input_data = np.array([[0, 0, 0, 0, bhk, size, price, price/size, 2000, 0, 0, floor, total_floors, 10, 2, 2, 1, parking, 1, 1, 1, 1]])

if st.button("Predict"):
    prediction_clf = clf.predict(input_data)[0]
    prediction_reg = reg.predict(input_data)[0]

    if prediction_clf == 1:
        st.success("Good Investment")
    else:
        st.error("Not a Good Investment")

    st.write(f"Estimated Price after 5 years: {prediction_reg:.2f} Lakhs")
