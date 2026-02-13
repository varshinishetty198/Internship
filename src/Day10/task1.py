import pandas as pd

df = pd.read_csv('customer_orders.csv')

print("Missing values per column:")
print(df.isna().sum())

numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    median_value = df[col].median()
    df[col].fillna(median_value, inplace=True)

print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")

print(f"Shape before cleaning: {df.shape}")

df = df.drop_duplicates()

print(f"Shape after cleaning: {df.shape}")

print("\nCleaned DataFrame:")
print(df)
