import pandas as pd
import numpy as np

df = pd.read_csv(r"E:\Retail-Sales-Analytics\Dataset\raw_data\SampleSuperstore.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())

print("\nDupicate Rows:")
print(df.duplicated().sum())

print("\n Missing Values:")
print(df.isnull().sum())

print("\n Data Types")
print(df.dtypes)

# df["Order Date"]=pd.to_datetime(df["Order Date"])
# df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d-%m-%Y"
)
print(df.dtypes)

print(df["Order Date"].head(10))

print(df["Order Date"].dtype)

print(df["Order Date"].sample(20))
print(df["Order Date"].unique()[:20])

# Create Year
df["Order Year"] = df["Order Date"].dt.year

# Create Month Number
df["Order Month No"] = df["Order Date"].dt.month

# Create Month Name
df["Order Month"] = df["Order Date"].dt.month_name()

# Create Quarter
df["Quarter"] = "Q" + df["Order Date"].dt.quarter.astype(str)

# Create Day Name
df["Day"] = df["Order Date"].dt.day_name()

print(df[[
    "Order Date",
    "Order Year",
    "Order Month No",
    "Order Month",
    "Quarter",
    "Day"
]].head())

df.to_csv(
    "Dataset/cleaned_data/Cleaned_Superstore.csv",
    index=False
)
# Fill missing Postal Code values with 0
df["Postal Code"] = df["Postal Code"].fillna(0)

# Convert to integer
df["Postal Code"] = df["Postal Code"].astype(int)
print(df["Postal Code"].isnull().sum())

print("✅ Cleaned dataset saved successfully!")
# print(df["Postal Code"].isnull().sum())