import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#141E30,#243B55);
}

h1,h2,h3,label,p{
    color:white !important;
}

[data-testid="stMetricValue"]{
    color:#00FF99;
}

div[data-testid="metric-container"]{
    background-color:rgba(255,255,255,0.08);
    border-radius:15px;
    padding:15px;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:10px;
    background:#00C853;
    color:white;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#009624;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Model
# -------------------------------
model = pickle.load(open("model.pkl","rb"))

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🎓 Placement Prediction")

st.sidebar.info("""
### Student Placement Prediction

✔ Machine Learning

✔ Random Forest

✔ Streamlit

✔ AI Based Prediction
""")

# -------------------------------
# Title
# -------------------------------
st.title("🎓 Student Placement Prediction System")

st.write("Fill all student details and click **Predict**.")

st.markdown("---")

# -------------------------------
# Two Columns
# -------------------------------
col1,col2=st.columns(2)

with col1:

    cgpa=st.number_input("CGPA",0.0,10.0,8.0)

    internships=st.number_input("Internships",0,10,2)

    projects=st.number_input("Projects",0,20,3)

    workshops=st.number_input("Workshops",0,20,2)

    aptitude=st.slider("Aptitude Score",0,100,80)

with col2:

    softskills=st.slider("Soft Skills",0.0,5.0,4.0)

    extracurricular=st.selectbox(
        "Extracurricular Activities",
        ["No","Yes"]
    )

    training=st.selectbox(
        "Placement Training",
        ["No","Yes"]
    )

    ssc=st.slider("SSC Marks",0,100,85)

    hsc=st.slider("HSC Marks",0,100,80)

# Convert Yes/No

extracurricular=1 if extracurricular=="Yes" else 0
training=1 if training=="Yes" else 0

st.markdown("---")

# -------------------------------
# Predict
# -------------------------------

if st.button("Predict Placement"):

    student=np.array([[

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

    prediction=model.predict(student)

    probability=model.predict_proba(student)

    placed=probability[0][1]*100

    # Result

    if prediction[0]==1:

        st.success("🎉 Student is Likely to be Placed")

        st.balloons()

    else:

        st.error("❌ Student is Not Likely to be Placed")

    # Probability

    st.subheader("📈 Placement Probability")

    st.progress(int(placed))

    st.metric(
        label="Chance of Placement",
        value=f"{placed:.2f}%"
    )

    # Student Score Card

    st.markdown("---")

    st.subheader("🏆 Student Score Card")

    c1,c2,c3=st.columns(3)

    c1.metric("CGPA",cgpa)

    c2.metric("Projects",projects)

    c3.metric("Internships",internships)

    st.bar_chart({
        "Marks":[ssc,hsc,aptitude]
    })

st.markdown("---")

st.caption("© 2026 Student Placement Prediction System")
