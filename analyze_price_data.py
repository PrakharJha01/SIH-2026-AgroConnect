"""
Analyze Price.csv data to understand structure for ML model.
"""
import pandas as pd
import numpy as np
from datetime import datetime

# Load the data
df = pd.read_csv('data/seed/Price.csv')

print("="*60)
print("PRICE DATA ANALYSIS")
print("="*60)

print(f"\nTotal rows: {len(df):,}")
print(f"Columns: {list(df.columns)}")

print("\n" + "="*60)
print("DATA STRUCTURE")
print("="*60)
print(df.dtypes)

print("\n" + "="*60)
print("SAMPLE DATA")
print("="*60)
print(df.head(10))

print("\n" + "="*60)
print("DATE INFORMATION")
print("="*60)
print(f"Date column: Arrival_Date")
print(f"Date range: {df['Arrival_Date'].min()} to {df['Arrival_Date'].max()}")
print(f"Unique dates: {df['Arrival_Date'].nunique()}")

print("\n" + "="*60)
print("COMMODITY INFORMATION")
print("="*60)
print(f"Unique commodities: {df['Commodity'].nunique()}")
print(f"Top 10 commodities by frequency:")
print(df['Commodity'].value_counts().head(10))

print("\n" + "="*60)
print("LOCATION INFORMATION")
print("="*60)
print(f"Unique states: {df['State'].nunique()}")
print(f"Unique markets: {df['Market'].nunique()}")

print("\n" + "="*60)
print("PRICE INFORMATION")
print("="*60)
print(f"Price columns: Min_x0020_Price, Max_x0020_Price, Modal_x0020_Price")
print("\nPrice statistics (Modal Price):")
print(df['Modal_x0020_Price'].describe())

print("\n" + "="*60)
print("MISSING VALUES")
print("="*60)
print(df.isnull().sum())

print("\n" + "="*60)
print("POTATO DATA (for our demo)")
print("="*60)
potato_data = df[df['Commodity'].str.contains('Potato', case=False, na=False)]
print(f"Potato records: {len(potato_data)}")
if len(potato_data) > 0:
    print("\nPotato data sample:")
    print(potato_data.head())
