import pandas as pd

data = {
    'Location': [' New York', 'new york', 'NEW YORK ', 'Los Angeles', ' los angeles ']
}
df = pd.DataFrame(data)

df['Location'] = df['Location'].str.strip()

df['Location'] = df['Location'].str.title()

print(df['Location'].unique())
