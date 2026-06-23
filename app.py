import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model.pkl")

product_encoder = joblib.load("product_encoder.pkl")
month_encoder = joblib.load("month_encoder.pkl")
promotion_encoder = joblib.load("promotion_encoder.pkl")
festival_encoder = joblib.load("festival_encoder.pkl")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Electronics Demand Forecasting",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Electronics Store Demand Forecasting Platform")

st.markdown(
"""
Predict the future demand of electronic products using Machine Learning.
"""
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Enter Product Details")

product = st.sidebar.selectbox(
    "Select Product",
    [
        "Air Conditioner",
        "Air Cooler",
        "Refrigerator",
        "Washing Machine",
        "Smart TV",
        "Laptop",
        "Microwave Oven",
        "Water Purifier",
        "Ceiling Fan",
        "Room Heater"
    ]
)

month = st.sidebar.selectbox(
    "Select Month",
    [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]
)

promotion = st.sidebar.selectbox(
    "Promotion",
    ["Yes","No"]
)

festival = st.sidebar.selectbox(
    "Festival Season",
    ["Yes","No"]
)

discount = st.sidebar.slider(
    "Discount (%)",
    0,
    40,
    10
)

previous_sales = st.sidebar.number_input(
    "Previous Month Sales",
    min_value=0,
    value=100
)

inventory = st.sidebar.number_input(
    "Current Inventory",
    min_value=0,
    value=120
)

predict = st.sidebar.button("🔮 Predict Demand")

# -----------------------------
# Main Page
# -----------------------------

st.subheader("Prediction Result")

if predict:

    # Encode Inputs
    product_value = product_encoder.transform([product])[0]
    month_value = month_encoder.transform([month])[0]
    promotion_value = promotion_encoder.transform([promotion])[0]
    festival_value = festival_encoder.transform([festival])[0]

    # Create Input DataFrame
    input_data = pd.DataFrame({
        "Product": [product_value],
        "Month": [month_value],
        "Promotion": [promotion_value],
        "Festival_Season": [festival_value],
        "Discount": [discount],
        "Previous_Month_Sales": [previous_sales]
    })

    # -----------------------------
    # Predict Demand Factor
    # -----------------------------
    predicted_factor = model.predict(input_data)[0]

    # Calculate Final Demand
    predicted_demand = round(previous_sales * predicted_factor)

    # Safety Checks
    if predicted_demand < 0:
        predicted_demand = 0

    # Maximum 50% increase over previous month
    max_demand = round(previous_sales * 1.5)

    if predicted_demand > max_demand:
        predicted_demand = max_demand

    # Create 3 Cards
    col1, col2, col3 = st.columns(3)

    # Card 1
    with col1:
        st.metric(
            "📦 Predicted Demand",
            f"{predicted_demand} Units"
        )

    # Card 2
    with col2:

        if inventory >= predicted_demand:
            status = "Sufficient"
        else:
            status = "Low Stock"

        st.metric(
            "📊 Inventory Status",
            status
        )

    # Card 3
    with col3:

        if inventory >= predicted_demand:
            restock = 0
        else:
            restock = predicted_demand - inventory

        st.metric(
            "⚠ Restock Needed",
            f"{restock} Units"
        )
    st.markdown("---")
    st.subheader("📋 Prediction Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Product",
            "Month",
            "Promotion",
            "Festival Season",
            "Discount (%)",
            "Previous Month Sales",
            "Current Inventory",
            "Predicted Demand"
        ],
        "Value": [
            product,
            month,
            promotion,
            festival,
            f"{discount} %",
            f"{previous_sales} Units",
            f"{inventory} Units",
            f"{predicted_demand} Units"
        ]
    })

    st.table(summary)
    


else:

    st.info("Please enter the details and click Predict Demand.")
    

# ---------------------------------
# Product-wise Sales Distribution
# ---------------------------------
sales_data = pd.read_csv("electronics_sales.csv")
st.markdown("---")
st.subheader("📊 Product-wise Average Sales")

product_sales = (
    sales_data.groupby("Product")["Sales"]
    .mean()
    .round()
    .reset_index()
)
fig2 = px.bar(
    product_sales,
    x="Product",
    y="Sales",
    color="Sales",
    text_auto=".1f",
    title="Average Sales by Product"
)

fig2.update_layout(
    xaxis_title="Product",
    yaxis_title="Average Sales"
)

st.plotly_chart(fig2, use_container_width=True)
