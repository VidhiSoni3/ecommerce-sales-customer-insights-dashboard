# E-Commerce Sales and Customer Insights Dashboard

## 1. Project Overview

This project analyzes e-commerce sales data to understand sales performance, profitability, product performance, and regional performance.

The project converts raw sales data into useful business insights through data analysis and visualization using Python and Streamlit.

## 2. Problem Statement

E-commerce businesses generate large amounts of sales data. Without proper analysis, it can be difficult to identify high-performing products, profitable categories, strong regions, and areas that need improvement.

This project analyzes e-commerce data and presents the results through an interactive dashboard to support data-driven business decisions.

## 3. Objectives

- Analyze overall sales performance.
- Calculate important business KPIs.
- Identify high-performing product categories.
- Analyze sales across different regions.
- Identify top-selling and profitable products.
- Analyze monthly sales trends.
- Analyze product and regional profitability.
- Generate useful business insights and recommendations.

## 4. Dataset

The dataset used in this project is the **E-Commerce Orders and Sales Performance Dataset** from Kaggle.

**Dataset Link:**  
https://www.kaggle.com/datasets/zahranusratt/e-commerce-orders-and-sales-performance-dataset

The dataset contains **3,500 transactions** and the following columns:

- Order Date
- Product Name
- Category
- Region
- Quantity
- Sales
- Profit

## 5. Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit

## 6. Key Performance Indicators

The dashboard displays the following KPIs:

- Total Sales
- Total Profit
- Total Orders
- Average Order Value

## 7. Dashboard Features

### Sales Analysis

- Sales by Category
- Sales by Region
- Monthly Sales Trend

### Profit Analysis

- Profit by Category
- Profit by Region
- Profit by Product

### Product Analysis

- Sales by Product
- Profit by Product

### Dataset Analysis

- Number of transactions
- Number of columns
- Total quantity sold
- Date range
- Missing-value check

### Business Insights

The dashboard provides key findings and business recommendations based on the analysis.

## 8. Key Findings

- Electronics is the highest-selling category.
- West is the highest-selling region.
- Camera is the top-selling product.
- Camera is also the most profitable product.
- Electronics generates the highest category profit.
- West generates the highest regional profit.
- The average order value is approximately ₹3,047.97.

## 9. Project Files

The repository contains the following project files:

- `VidhiSoni_ECommerceSalesCustomerInsightsDashboard.py` — Complete project code and Streamlit dashboard
- `requirements.txt` — Required Python libraries and dependencies
- `VidhiSoni_ProjectReport.docx` — Complete project report
- `README.md` — Project documentation and setup instructions
- `ecommerce_sales_data (2).csv` — Dataset used for the analysis

## 10. How to Run the Project

### Step 1: Clone or Download the Repository

Download the project repository to your computer.

### Step 2: Install Required Libraries

Open Command Prompt or Terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Dashboard

Run the following command:

```bash
streamlit run VidhiSoni_ECommerceSalesCustomerInsightsDashboard.py
```

### Step 4: Open the Dashboard

After running the command, Streamlit will provide a local URL.

Open the provided URL in a web browser to view the interactive dashboard.

## 11. Key Business Insights

The analysis shows that Electronics contributes the highest sales and profit among the categories.

The West region records the highest sales and profit among the regions.

Camera is the top-selling as well as the most profitable product.

These findings can support decisions related to inventory planning, marketing focus, regional sales strategies, and product performance monitoring.

## 12. Business Recommendations

- Maintain sufficient stock of high-performing products.
- Focus marketing efforts on strong-performing categories.
- Analyze opportunities to increase sales in lower-performing regions.
- Monitor product and regional profitability regularly.
- Use monthly sales trends to support inventory and promotional planning.

## 13. Conclusion

The project demonstrates how raw e-commerce transaction data can be transformed into meaningful business insights using Python, Pandas, and Streamlit.

The interactive dashboard helps users understand sales, profit, product, and regional performance and supports data-driven business decision-making.
