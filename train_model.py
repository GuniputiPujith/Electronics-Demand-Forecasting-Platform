import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("electronics_sales.csv")

# -----------------------------
# Label Encoding
# -----------------------------
product_encoder = LabelEncoder()
month_encoder = LabelEncoder()
promotion_encoder = LabelEncoder()
festival_encoder = LabelEncoder()

df["Product"] = product_encoder.fit_transform(df["Product"])
df["Month"] = month_encoder.fit_transform(df["Month"])
df["Promotion"] = promotion_encoder.fit_transform(df["Promotion"])
df["Festival_Season"] = festival_encoder.fit_transform(df["Festival_Season"])

# -----------------------------
# Features
# -----------------------------
X = df[
    [
        "Product",
        "Month",
        "Promotion",
        "Festival_Season",
        "Discount",
        "Previous_Month_Sales"
    ]
]

# -----------------------------
# Target
# -----------------------------
y = df["Demand_Factor"]

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
pred = model.predict(X_test)

print("R2 Score :", r2_score(y_test, pred))

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "model.pkl")
joblib.dump(product_encoder, "product_encoder.pkl")
joblib.dump(month_encoder, "month_encoder.pkl")
joblib.dump(promotion_encoder, "promotion_encoder.pkl")
joblib.dump(festival_encoder, "festival_encoder.pkl")

print("Model Saved Successfully!")