import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="SkillSync Project Engine",
    page_icon="🚀",
    layout="centered"
)

st.sidebar.title("About")

st.sidebar.info(
    "SkillSync Project Engine is an AI-powered recommendation system "
    "that helps students discover suitable technical project domains."
)

# Load trained model
model = joblib.load("model/model.pkl")

# Recommendation data
recommendations = {
    "Machine Learning": {
        "projects": [
            "AI Chatbot",
            "House Price Prediction",
            "Student Performance Predictor"
        ],
        "tech_stack": [
            "Python",
            "Scikit-learn",
            "Pandas",
            "Streamlit"
        ]
    },

    "Web Development": {
        "projects": [
            "Portfolio Website",
            "E-commerce Website",
            "Blog Platform"
        ],
        "tech_stack": [
            "HTML",
            "CSS",
            "JavaScript",
            "React"
        ]
    },

    "Cybersecurity": {
        "projects": [
            "Password Strength Checker",
            "Network Scanner",
            "Phishing Detection System"
        ],
        "tech_stack": [
            "Python",
            "Linux",
            "Wireshark",
            "Networking"
        ]
    },

    "Cloud Computing": {
        "projects": [
            "Cloud Storage System",
            "DevOps Automation",
            "Virtual Machine Manager"
        ],
        "tech_stack": [
            "AWS",
            "Docker",
            "Linux",
            "Kubernetes"
        ]
    },

    "Java Development": {
        "projects": [
            "Library Management System",
            "Banking Application",
            "Student Management System"
        ],
        "tech_stack": [
            "Java",
            "MySQL",
            "Spring Boot"
        ]
    },

    "Data Analytics": {
        "projects": [
            "Sales Dashboard",
            "Customer Analysis System",
            "Market Trend Analyzer"
        ],
        "tech_stack": [
            "Python",
            "SQL",
            "Power BI",
            "Pandas"
        ]
    },

    "Android Development": {
        "projects": [
            "To-Do App",
            "Fitness Tracker",
            "Expense Manager"
        ],
        "tech_stack": [
            "Java",
            "Kotlin",
            "Android Studio"
        ]
    }
}

le_interest = joblib.load("model/le_interest.pkl")
le_skills = joblib.load("model/le_skills.pkl")
le_subject = joblib.load("model/le_subject.pkl")
le_experience = joblib.load("model/le_experience.pkl")
le_goal = joblib.load("model/le_goal.pkl")
le_domain = joblib.load("model/le_domain.pkl")

# Streamlit UI
st.title("SkillSync Project Engine")
st.markdown("---")

st.write("AI-powered system for recommending technical project domains.")

# User Inputs
interest = st.selectbox(
    "Select Your Interest",
    ["AI", "Web Apps", "Security", "Cloud", "Data Analysis", "Android", "Automation", "Networking", "UI Design", "Java"]
)

skills = st.selectbox(
    "Select Your Skill",
    ["Python", "Java", "HTML CSS JavaScript", "Linux", "AWS", "SQL", "TensorFlow", "React", "Docker", "Kotlin"]
)

subject = st.selectbox(
    "Favorite Subject",
    ["Data Science", "Web Technology", "Cyber Security", "Cloud Computing", "Java Programming", "Statistics", "Software Engineering", "Networking", "Mobile Computing", "AI"]
)

experience = st.selectbox(
    "Experience Level",
    ["Beginner", "Intermediate", "Advanced"]
)

goal = st.selectbox(
    "Career Goal",
    ["ML Engineer", "Frontend Developer", "Security Analyst", "Cloud Engineer", "Backend Developer", "Data Analyst", "Android Developer", "DevOps Engineer"]
)

# Predict Button
if st.button("Recommend Domain"):

    # Convert inputs into dataframe
    input_data = pd.DataFrame({
    "Interest": le_interest.transform([interest]),
    "Skills": le_skills.transform([skills]),
    "Favorite_Subject": le_subject.transform([subject]),
    "Experience_Level": le_experience.transform([experience]),
    "Career_Goal": le_goal.transform([goal])
})

    # Predict
    prediction = model.predict(input_data)[0]

    predicted_domain = le_domain.inverse_transform([prediction])[0]

    st.markdown("## Recommendation Results")

    st.success(f"Recommended Domain: {predicted_domain}")

    st.subheader("Suggested Projects")
    for project in recommendations[predicted_domain]["projects"]:
        st.write(f"- {project}")

    st.subheader("Recommended Tech Stack")
    for tech in recommendations[predicted_domain]["tech_stack"]:
        st.write(f"- {tech}")
    st.markdown("---")
    st.caption("Built using Python, Scikit-learn, Streamlit & Machine Learning")