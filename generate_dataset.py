import pandas as pd
import random
products = [
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
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
season_factor = {

    "Air Conditioner": {
        "January":0.40,"February":0.50,"March":0.80,"April":1.00,
        "May":1.30,"June":1.25,"July":1.10,"August":1.00,
        "September":0.80,"October":0.60,"November":0.45,"December":0.40
    },

    "Air Cooler": {
        "January":0.30,"February":0.40,"March":0.70,"April":1.00,
        "May":1.25,"June":1.20,"July":1.00,"August":0.90,
        "September":0.70,"October":0.45,"November":0.30,"December":0.25
    },

    "Ceiling Fan": {
        "January":0.60,"February":0.70,"March":0.90,"April":1.10,
        "May":1.20,"June":1.20,"July":1.10,"August":1.00,
        "September":0.90,"October":0.80,"November":0.70,"December":0.60
    },

    "Room Heater": {
        "January":1.30,"February":1.15,"March":0.70,"April":0.40,
        "May":0.25,"June":0.20,"July":0.20,"August":0.25,
        "September":0.40,"October":0.70,"November":1.10,"December":1.35
    },

    "Refrigerator": {
        month:1.00 for month in months
    },

    "Washing Machine": {
        month:1.00 for month in months
    },

    "Smart TV": {
        "January":0.90,"February":0.90,"March":0.90,"April":0.95,
        "May":0.95,"June":1.00,"July":1.00,"August":1.05,
        "September":1.10,"October":1.35,"November":1.30,"December":1.20
    },

    "Laptop": {
        "January":0.90,"February":0.90,"March":0.95,"April":1.00,
        "May":1.00,"June":1.15,"July":1.25,"August":1.30,
        "September":1.15,"October":1.10,"November":1.20,"December":1.10
    },

    "Microwave Oven": {
        "January":0.80,"February":0.80,"March":0.85,"April":0.90,
        "May":0.90,"June":0.95,"July":1.00,"August":1.00,
        "September":1.10,"October":1.30,"November":1.35,"December":1.20
    },

    "Water Purifier": {
        "January":0.70,"February":0.80,"March":1.00,"April":1.15,
        "May":1.25,"June":1.20,"July":1.10,"August":1.00,
        "September":0.90,"October":0.80,"November":0.75,"December":0.70
    }

}
# Base Average Sales of each product
base_sales = {
    "Air Conditioner": 200,
    "Air Cooler": 180,
    "Refrigerator": 220,
    "Washing Machine": 200,
    "Smart TV": 210,
    "Laptop": 215,
    "Microwave Oven": 190,
    "Water Purifier": 185,
    "Ceiling Fan": 205,
    "Room Heater": 160
}

data = []

for i in range(2000):

    product = random.choice(products)
    month = random.choice(months)

    promotion = random.choice(["Yes", "No"])
    festival = random.choice(["Yes", "No"])

    discount = random.randint(0, 40)

    # Base Seasonal Factor
    factor = season_factor[product][month]

    # Previous Month Sales
    previous_sales = random.randint(80, 250)

    # Save the ORIGINAL seasonal factor
    demand_factor = factor

    # Calculate Sales using seasonal factor
    sales = previous_sales * factor

    # Promotion Effect
    if promotion == "Yes":
        sales *= random.uniform(1.10, 1.20)

    # Festival Effect
    if festival == "Yes":
        sales *= random.uniform(1.08, 1.15)

    # Discount Effect
    sales *= (1 + discount * 0.003)

    # Small Random Noise
    sales += random.randint(-5, 5)

    sales = round(sales)

    data.append([
        product,
        month,
        promotion,
        festival,
        discount,
        previous_sales,
        round(demand_factor,3),
        sales
    ])
# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Product",
        "Month",
        "Promotion",
        "Festival_Season",
        "Discount",
        "Previous_Month_Sales",
        "Demand_Factor",
        "Sales"
    ]
)

# Save Dataset
df.to_csv("electronics_sales.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())