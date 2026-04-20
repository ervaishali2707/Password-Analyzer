import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "password": ["12345", "password", "Pass@123", "Strong#789", "hello123", "Admin@2024"],
    "label": [0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

def extract_features(pw):
    return [
        len(pw),
        sum(c.isdigit() for c in pw),
        sum(c.isupper() for c in pw),
        sum(not c.isalnum() for c in pw)
    ]

X = df["password"].apply(extract_features).tolist()
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "password_model.pkl")

print("Model trained!")