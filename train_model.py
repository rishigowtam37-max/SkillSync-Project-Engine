import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("data/students.csv")

# Create Label Encoders
le_interest = LabelEncoder()
le_skills = LabelEncoder()
le_subject = LabelEncoder()
le_experience = LabelEncoder()
le_goal = LabelEncoder()
le_domain = LabelEncoder()

# Encode columns
df["Interest"] = le_interest.fit_transform(df["Interest"])
df["Skills"] = le_skills.fit_transform(df["Skills"])
df["Favorite_Subject"] = le_subject.fit_transform(df["Favorite_Subject"])
df["Experience_Level"] = le_experience.fit_transform(df["Experience_Level"])
df["Career_Goal"] = le_goal.fit_transform(df["Career_Goal"])
df["Recommended_Domain"] = le_domain.fit_transform(df["Recommended_Domain"])

# Features and target
X = df.drop("Recommended_Domain", axis=1)
y = df["Recommended_Domain"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "model/model.pkl")
joblib.dump(le_interest, "model/le_interest.pkl")
joblib.dump(le_skills, "model/le_skills.pkl")
joblib.dump(le_subject, "model/le_subject.pkl")
joblib.dump(le_experience, "model/le_experience.pkl")
joblib.dump(le_goal, "model/le_goal.pkl")
joblib.dump(le_domain, "model/le_domain.pkl")

print("Model saved successfully!")