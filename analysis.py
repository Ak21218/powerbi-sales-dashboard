import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# -------------------------
# Day 1 (Basic info)
# -------------------------

print(df.head())

print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nInfo:")
df.info()

# -------------------------
# Day 2 (Data Cleaning + EDA)
# -------------------------

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Data types
print("\nData Types:")
print(df.dtypes)

# Summary stats
print("\nSummary Statistics:")
print(df.describe())

# -------------------------
# Analysis
# -------------------------

# Total sales & profit
print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

# Sales by Region
print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

# Sales by Category
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())


