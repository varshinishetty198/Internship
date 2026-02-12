import pandas as pd

# 1️⃣ Load the dataset
df = pd.read_csv('customer_orders.csv')

# 2️⃣ Check for missing values
print("Missing values per column:")
print(df.isna().sum())

# 3️⃣ Handle missing numeric values by filling with median
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    median_value = df[col].median()
    df[col].fillna(median_value, inplace=True)

# 4️⃣ Check for duplicates
print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")

# 5️⃣ Print shape before cleaning
print(f"Shape before cleaning: {df.shape}")

# 6️⃣ Remove duplicate rows
df = df.drop_duplicates()

# 7️⃣ Print shape after cleaning
print(f"Shape after cleaning: {df.shape}")

# ✅ Optional: view the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)
