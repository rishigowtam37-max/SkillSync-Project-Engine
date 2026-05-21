import pandas as pd
import random

interests = [
    "AI",
    "Web Apps",
    "Security",
    "Cloud",
    "Data Analysis",
    "Android",
    "Automation",
    "Networking",
    "UI Design",
    "Java"
]

skills = [
    "Python",
    "Java",
    "HTML CSS JavaScript",
    "Linux",
    "AWS",
    "SQL",
    "TensorFlow",
    "React",
    "Docker",
    "Kotlin"
]

subjects = [
    "Data Science",
    "Web Technology",
    "Cyber Security",
    "Cloud Computing",
    "Java Programming",
    "Statistics",
    "Software Engineering",
    "Networking",
    "Mobile Computing",
    "AI"
]

experience_levels = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

career_goals = [
    "ML Engineer",
    "Frontend Developer",
    "Security Analyst",
    "Cloud Engineer",
    "Backend Developer",
    "Data Analyst",
    "Android Developer",
    "DevOps Engineer"
]

domains = {
    "AI": "Machine Learning",
    "Data Analysis": "Data Analytics",
    "Security": "Cybersecurity",
    "Cloud": "Cloud Computing",
    "Java": "Java Development",
    "Web Apps": "Web Development",
    "Android": "Android Development",
    "Automation": "Machine Learning",
    "Networking": "Cybersecurity",
    "UI Design": "Web Development"
}

data = []

for _ in range(500):
    interest = random.choice(interests)

    row = {
        "Interest": interest,
        "Skills": random.choice(skills),
        "Favorite_Subject": random.choice(subjects),
        "Experience_Level": random.choice(experience_levels),
        "Career_Goal": random.choice(career_goals),
        "Recommended_Domain": domains[interest]
    }

    data.append(row)

df = pd.DataFrame(data)

df.to_csv("data/students.csv", index=False)

print("500-row dataset created successfully!")