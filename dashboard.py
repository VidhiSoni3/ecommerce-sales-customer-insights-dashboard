import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_sales_data (2).csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Dashboard title
st.title("E-Commerce Sales & Customer Insights Dashboard")

st.write("Analysis of sales, profit, products and regional performance.")

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_order_value = total_sales / total_orders

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
col4.metric("Average Order Value", f"₹{average_order_value:,.2f}")
# Sales Analysis

st.header("Sales Analysis")

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

st.subheader("Sales by Category")
st.bar_chart(category_sales)

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

st.subheader("Sales by Region")
st.bar_chart(region_sales)
# Monthly Sales Trend

st.header("Monthly Sales Trend")

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)
# Profit Analysis

st.header("Profit Analysis")

profit_category = df.groupby("Category")["Profit"].sum()

st.subheader("Profit by Category")
st.bar_chart(profit_category)

profit_region = df.groupby("Region")["Profit"].sum()

st.subheader("Profit by Region")
st.bar_chart(profit_region)
# Product Analysis

st.header("Product Analysis")

product_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

st.subheader("Sales by Product")
st.bar_chart(product_sales)

product_profit = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False)

st.subheader("Profit by Product")
st.bar_chart(product_profit)
# Key Insights and Recommendations

st.header("Key Insights & Recommendations")

st.subheader("Key Insights")

st.write("• Electronics is the highest-selling category.")
st.write("• West is the highest-selling region.")
st.write("• Camera is the top-selling and most profitable product.")
st.write("• Electronics generates the highest category profit.")
st.write("• West generates the highest regional profit.")
st.write("• Average Order Value is ₹3,047.97.")

st.subheader("Business Recommendations")

st.write("• Maintain sufficient stock of high-performing products.")
st.write("• Focus marketing efforts on strong-performing categories.")
st.write("• Analyze opportunities to increase sales in lower-performing regions.")
st.write("• Monitor product and regional profitability regularly.")