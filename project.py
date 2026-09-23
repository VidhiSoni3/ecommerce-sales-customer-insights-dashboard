import pandas as pd

df = pd.read_csv("ecommerce_sales_data (2).csv")

print("FIRST 5 ROWS:")
print(df.head())

print("\nDATASET SIZE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nMISSING VALUES:")
print(df.isnull().sum())
print("\nKEY PERFORMANCE INDICATORS:")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = len(df)

print("Total Sales:", total_sales)
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
print("\nKEY PERFORMANCE INDICATORS:")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = len(df)

print("Total Sales:", total_sales)
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
print("\nSALES BY CATEGORY:")

category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)
print("\nSALES BY PRODUCT:")

product_sales = df.groupby("Product Name")["Sales"].sum()

print(product_sales)
print("\nSALES BY REGION:")

region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)
print("\nMONTHLY SALES:")

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

print(monthly_sales)
import matplotlib.pyplot as plt

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
print("\nPROFIT BY CATEGORY:")

category_profit = df.groupby("Category")["Profit"].sum()

print(category_profit)
print("\nPROFIT BY REGION:")

region_profit = df.groupby("Region")["Profit"].sum()

print(region_profit)
print("\nTOP SELLING PRODUCT:")

top_product = df.groupby("Product Name")["Sales"].sum().idxmax()
top_product_sales = df.groupby("Product Name")["Sales"].sum().max()

print("Product:", top_product)
print("Sales:", top_product_sales)
print("\nMOST PROFITABLE PRODUCT:")

product_profit = df.groupby("Product Name")["Profit"].sum()

top_profit_product = product_profit.idxmax()
top_profit = product_profit.max()

print("Product:", top_profit_product)
print("Profit:", round(top_profit, 2))
print("\nAVERAGE ORDER VALUE:")

average_order_value = df["Sales"].sum() / len(df)

print("Average Order Value:", round(average_order_value, 2))
print("\nSALES BY CATEGORY GRAPH:")

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()
print("\nSALES BY REGION GRAPH:")

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()
print("\nPROFIT BY CATEGORY GRAPH:")

category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()
print("\nPROFIT BY REGION GRAPH:")

region_profit.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()
print("\n========== FINAL INSIGHTS ==========")

# Top category by sales
top_category = category_sales.idxmax()
print("Top Sales Category:", top_category)

# Top region by sales
top_region = region_sales.idxmax()
print("Top Sales Region:", top_region)

# Top product by sales
print("Top Selling Product:", top_product)

# Top product by profit
print("Most Profitable Product:", top_profit_product)

# Highest profit category
highest_profit_category = category_profit.idxmax()
print("Highest Profit Category:", highest_profit_category)

# Highest profit region
highest_profit_region = region_profit.idxmax()
print("Highest Profit Region:", highest_profit_region)

# Average Order Value
print("Average Order Value:", round(average_order_value, 2))