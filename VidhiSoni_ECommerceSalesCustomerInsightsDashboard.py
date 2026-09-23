import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# E-Commerce Sales and Customer Insights Dashboard
# Prepared by: Vidhi Soni

st.set_page_config(
    page_title="E-Commerce Sales & Customer Insights Dashboard",
    page_icon="📊",
    layout="wide"
)

DATA_FILE = "ecommerce_sales_data (2).csv"

# 1. Load and prepare data
df = pd.read_csv(DATA_FILE)
df["Order Date"] = pd.to_datetime(df["Order Date"])

# 2. Dataset checks
missing_values = df.isnull().sum()

# 3. Key Performance Indicators
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = len(df)
average_order_value = total_sales / total_orders

# 4. Sales and profit analysis
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()
monthly_sales.index = monthly_sales.index.astype(str)

category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

product_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
product_profit = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False)

# 5. Top performers
top_product = product_sales.idxmax()
top_product_sales = product_sales.max()
most_profitable_product = product_profit.idxmax()
most_profitable_product_profit = product_profit.max()
top_category = category_sales.idxmax()
top_region = region_sales.idxmax()
highest_profit_category = category_profit.idxmax()
highest_profit_region = region_profit.idxmax()

# 6. Dashboard title
st.title("E-Commerce Sales & Customer Insights Dashboard")
st.write(
    "Analysis of e-commerce sales data to understand sales performance, "
    "profitability, product performance, regional performance, and business opportunities."
)

# 7. KPI section
st.header("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Average Order Value", f"₹{average_order_value:,.2f}")

# 8. Dataset summary
st.header("Dataset Summary")
summary_col1, summary_col2 = st.columns(2)

with summary_col1:
    st.write("**Number of Transactions:**", len(df))
    st.write("**Number of Columns:**", len(df.columns))
    st.write("**Total Quantity Sold:**", f"{total_quantity:,}")

with summary_col2:
    st.write("**Date Range:**")
    st.write(
        f"{df['Order Date'].min().date()} to "
        f"{df['Order Date'].max().date()}"
    )

if missing_values.sum() == 0:
    st.success("Dataset check: No missing values found.")
else:
    st.warning("Dataset contains missing values.")
    st.dataframe(missing_values)

# 9. Sales analysis
st.header("Sales Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    st.bar_chart(category_sales)

with col2:
    st.subheader("Sales by Region")
    st.bar_chart(region_sales)

# 10. Monthly sales trend
st.header("Monthly Sales Trend")
st.line_chart(monthly_sales)

# 11. Profit analysis
st.header("Profit Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Profit by Category")
    st.bar_chart(category_profit)

with col2:
    st.subheader("Profit by Region")
    st.bar_chart(region_profit)

# 12. Product analysis
st.header("Product Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Product")
    st.bar_chart(product_sales)

with col2:
    st.subheader("Profit by Product")
    st.bar_chart(product_profit)

# 13. Key insights and recommendations
st.header("Key Insights & Recommendations")
st.subheader("Key Insights")

st.write(f"• {top_category} is the highest-selling category.")
st.write(f"• {top_region} is the highest-selling region.")
st.write(
    f"• {top_product} is the top-selling product "
    f"with sales of ₹{top_product_sales:,.0f}."
)
st.write(
    f"• {most_profitable_product} is the most profitable product "
    f"with profit of ₹{most_profitable_product_profit:,.2f}."
)
st.write(f"• {highest_profit_category} generates the highest category profit.")
st.write(f"• {highest_profit_region} generates the highest regional profit.")
st.write(f"• The Average Order Value is ₹{average_order_value:,.2f}.")

st.subheader("Business Recommendations")
st.write("• Maintain sufficient stock of high-performing products.")
st.write("• Focus marketing efforts on strong-performing categories.")
st.write("• Analyze opportunities to increase sales in lower-performing regions.")
st.write("• Monitor product and regional profitability regularly.")
st.write("• Use monthly sales trends to support inventory and promotional planning.")

# 14. Detailed analysis tables
st.header("Detailed Analysis Tables")

with st.expander("View Sales by Category"):
    st.dataframe(category_sales.rename("Sales"))

with st.expander("View Sales by Region"):
    st.dataframe(region_sales.rename("Sales"))

with st.expander("View Sales by Product"):
    st.dataframe(product_sales.rename("Sales"))

with st.expander("View Profit by Category"):
    st.dataframe(category_profit.rename("Profit"))

with st.expander("View Profit by Region"):
    st.dataframe(region_profit.rename("Profit"))

with st.expander("View Profit by Product"):
    st.dataframe(product_profit.rename("Profit"))

# 15. Project information
st.header("Project Information")
st.write("**Project:** E-Commerce Sales and Customer Insights Dashboard")
st.write("**Prepared by:** Vidhi Soni")
st.write("**Technologies:** Python, Pandas, Matplotlib, Streamlit")

st.caption(
    "This dashboard transforms raw e-commerce transaction data into "
    "KPIs, visual analysis, business insights, and recommendations."
)
