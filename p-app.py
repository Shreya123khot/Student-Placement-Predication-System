import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🎓 Student Placement Prediction System")

# Input Fields
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0)

internships = st.number_input("Internships", min_value=0)

projects = st.number_input("Projects", min_value=0)

workshops = st.number_input("Workshops/Certifications", min_value=0)

aptitude = st.number_input("Aptitude Test Score", min_value=0, max_value=100)

softskills = st.number_input("Soft Skills Rating", min_value=0.0, max_value=5.0)

extracurricular = st.selectbox(
    "Extracurricular Activities",
    [0, 1]
)

training = st.selectbox(
    "Placement Training",
    [0, 1]
)

ssc = st.number_input("SSC Marks", min_value=0, max_value=100)

hsc = st.number_input("HSC Marks", min_value=0, max_value=100)

# Prediction
if st.button("Predict"):

    input_data = np.array([[
        cgpa,
        internships,
        projects,
        workshops,
        aptitude,
        softskills,
        extracurricular,
        training,
        ssc,
        hsc
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Student is Likely to be Placed")
    else:
        st.error("❌ Student is Not Likely to be Placed")
