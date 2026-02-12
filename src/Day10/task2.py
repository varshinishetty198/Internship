import pandas as pd

data = {
    'Price': ['$100.50', '$200.75', '$150.00'],
    'Date': ['2026-01-01', '2026-01-02', '2026-01-03']
}
df = pd.DataFrame(data)

print(df.dtypes)

df['Price'] = df['Price'].str.replace('$', '', regex=False).astype(float)

df['Date'] = pd.to_datetime(df['Date'])

print(df.dtypes)
print(df)
