import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


# ---------------- UI CONFIG ----------------
st.set_page_config(page_title="Placement Predictor", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
}
.card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Placement Prediction System")
st.write("AI based ML model using Random Forest")

# ---------------- SAMPLE DATA (training demo) ----------------
data = pd.DataFrame({
    "CGPA":[6,7,8,9,5,7.5,8.5,9.2],
    "Internships":[0,1,1,2,0,1,2,2],
    "Projects":[1,2,3,4,1,3,4,5],
    "Aptitude":[50,60,70,85,40,75,88,92],
    "Placed":[0,0,1,1,0,1,1,1]
})

X = data.drop("Placed", axis=1)
y = data["Placed"]

model = RandomForestClassifier()
model.fit(X, y)

# ---------------- INPUT ----------------
st.subheader("📌 Enter Student Details")

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
internships = st.slider("Internships", 0, 5, 1)
projects = st.slider("Projects", 0, 10, 2)
aptitude = st.slider("Aptitude Score", 0, 100, 60)

input_data = np.array([[cgpa, internships, projects, aptitude]])

# ---------------- PREDICTION ----------------
if st.button("Predict Placement"):
    result = model.predict(input_data)

    if result[0] == 1:
        st.success("🎉 Student is Likely to be PLACED!")
    else:
        st.error("❌ Student is NOT likely to be placed")

# ---------------- CHART ----------------
st.subheader("📊 Data Visualization")

fig, ax = plt.subplots()
ax.bar(["CGPA","Internships","Projects","Aptitude"], [cgpa, internships, projects, aptitude])
st.pyplot(fig)
