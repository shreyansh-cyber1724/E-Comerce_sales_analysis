📦 E-Commerce Sales Analysis

📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on an Amazon e-commerce sales dataset to understand revenue trends, delivery performance, and order behavior over time.
The analysis focuses on identifying business insights that can help improve logistics efficiency and revenue growth.

📂 Dataset Information

Source: Kaggle

Dataset Name: Amazon Sale Report

File Used: Amazon Sale Report.csv

Description: Contains order-level data including order date, courier status, order amount, currency, B2B flag, and shipping details.

🎯 Objectives

Clean and prepare raw e-commerce data

Analyze monthly revenue trends

Calculate unshipped order percentage

Compare B2B vs B2C orders

Analyze revenue per order

Visualize insights using Matplotlib

🛠️ Tools & Libraries

Python

Pandas – data cleaning & analysis

Matplotlib – data visualization

🔍 Key Steps Performed
1️⃣ Data Inspection

Checked dataset shape and structure

Identified missing values and duplicates

Reviewed data types and distributions

2️⃣ Data Cleaning

Removed rows with missing critical values (Amount, Currency, Courier Status, Ship City)

Cleaned text columns using str.strip() and standard formatting

Converted Date column to datetime format

Extracted month from date for time-based analysis

3️⃣ Feature Engineering

Created month column from order date

Standardized courier status values

Converted revenue into million INR for better visualization

📊 Analysis Performed
🚚 Logistics Performance

Monthly shipped vs unshipped orders

Calculated Unshipped Percentage per month
→ Helps identify logistics inefficiencies

💰 Revenue Analysis

Monthly total revenue

Revenue trend visualization

Revenue per order (average order value)

🏢 Business Type Analysis

Monthly B2B vs B2C order counts

📈 Visualizations

Monthly Revenue Trend (in Million INR)

Revenue per Order Trend

Comparative courier performance by month

💡 Key Insights

Revenue shows rapid growth after early months

Logistics performance worsens in some later months (higher unshipped %)

Revenue per order remains relatively stable

Majority of orders are B2C, with limited B2B contribution

📌 Author

Shreyansh Attri Rishi
