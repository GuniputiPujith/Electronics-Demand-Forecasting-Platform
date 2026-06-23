# 📊 Electronics Store Demand Forecasting Platform

## 📌 Project Overview

The **Electronics Store Demand Forecasting Platform** is a Machine Learning-based web application that predicts future demand for electronic products. It helps retailers estimate product demand, monitor inventory levels, and identify restocking requirements.

The application uses a **Random Forest Regressor** trained on a synthetic retail dataset with realistic seasonal demand patterns.

---

## 🚀 Features

* Predict product demand using Machine Learning
* Seasonal demand forecasting
* Inventory status prediction
* Restock recommendation
* Interactive Streamlit dashboard
* Product-wise average sales visualization

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Plotly
* Joblib
* Jupyter Notebook

---

## 🤖 Machine Learning Model

**Algorithm Used:**

* Random Forest Regressor

**Input Features**

* Product
* Month
* Promotion
* Festival Season
* Discount (%)
* Previous Month Sales

**Output**

* Predicted Demand
* Inventory Status
* Restock Needed

---

## 📂 Project Structure

```
Electronics-Demand-Forecasting-Platform/
│
├── app.py
├── generate_dataset.py
├── train_model.py
├── electronics_sales.csv
├── model.pkl
├── product_encoder.pkl
├── month_encoder.pkl
├── promotion_encoder.pkl
├── festival_encoder.pkl
├── requirements.txt
├── EDA.ipynb
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/GuniputiPujith/Electronics-Demand-Forecasting-Platform.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📈 Workflow

1. Generate Dataset
2. Perform Data Preprocessing
3. Train Random Forest Regressor
4. Evaluate Model
5. Save Model
6. Launch Streamlit Application
7. Predict Demand
8. Inventory Analysis
9. Restock Recommendation

---

## 📸 Application Features

* Product Selection
* Month Selection
* Promotion & Festival Options
* Discount Input
* Previous Month Sales
* Current Inventory
* Predicted Demand
* Inventory Status
* Restock Recommendation
* Product-wise Average Sales Chart

---

## 🔮 Future Enhancements

* Real retail sales database integration
* Weather-based demand forecasting
* Multi-store inventory prediction
* Cloud deployment
* Deep Learning based forecasting

---

## 👨‍💻 Author

**Guniputi Pujith**

B.Tech CSE (AI & ML)

Machine Learning | Python | Data Science
