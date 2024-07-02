## Aim for this module: 
![modeling the data](image.png)
---

## Excel.
1. [Correlation analysis](https://www.youtube.com/watch?v=lXHCyhO7DmY) shows the linear relation between variables.

    [workbook for correaltion using excel](https://docs.google.com/spreadsheets/d/1_vQF2i5ubKmHQMBqoTwsu6AlevWsQtTD/view#gid=790744269)

    - ***dont forget to check the add ins.***

2. [Regression with excel](https://www.youtube.com/watch?v=AERQBMIHwXA)

    [workbook for regression (model 1)](https://docs.google.com/spreadsheets/d/1YZLb9ozhmc-8KQ7EaaTgs57QT6dHju5u/view#gid=242862119)
    
    [workbook for regression (model 2 )](https://docs.google.com/spreadsheets/d/1KAolaOQC-P_6gXaw3jgUc7GWKAHfOrsi/view#gid=824457557)

3. [forecasting in excel](https://www.youtube.com/watch?v=QrTimmxwZw4)

4. [outlier detection with excel](https://www.youtube.com/watch?v=sUTJb0F9eBw)
---

## Python
### With parquet file.
- Parquet is a file format like Excel or CSV, but is fast, small, and great for analysis. 
```python
#reading a parquet file
import pandas as pd

df = pd.read_parquet("transactions.parquet")
df
```
- some of the useful functions in pandas to observe the dataset:
    1. .groupby()
    2. .pivot_table()

- pearson correlation also forms an important metric to analyse the data.
```python
import scipy 

pearson_correlation, p_value = scipy.stats.pearsonr(new_df['Approved'], new_df['Amount'])
print(f"Pearson correlation: {pearson_correlation}")
print(f"P-value: {p_value}")

# Check if the correlation is statistically significant
alpha = 0.05  # common significance level
if p_value < alpha:
    print("The correlation is statistically significant.")
else:
    print("The correlation is not statistically significant.")
```
- a good visualization for seeing How has the % of disputed transactions changed over time?
```python
df['Transaction Time'] = pd.to_timedelta(df['Transaction Time'])

# Combine Transaction Date and Transaction Time to create a datetime column
df['Transaction DateTime'] = df['Transaction Date'] + df['Transaction Time']

# Extract hour and day from the datetime column
df['Hour'] = df['Transaction DateTime'].dt.hour
df['Day'] = df['Transaction DateTime'].dt.date

# Create a pivot table
pivot_table = df.pivot_table(
    index='Hour',
    columns='Day',
    values='Decision',
    aggfunc=lambda x: (x == 'Approved').mean() * 100
)

# Display the pivot table
pivot_table

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="RdYlGn", cbar_kws={'label': 'Approval Percentage'})
plt.title('Approval Percentage by Hour and Day')
plt.xlabel('Day')
plt.ylabel('Hour of Day')
plt.show()
```
![the heatmap of correlation](image-1.png)

### With databases.

- the way to access the database is to query it using SQL, using pandas and sqlalchemy
```python
import pandas as pd
import sqlalchemy as sa
import numpy as np

engine = sa.create_engine("mysql+pymysql://guest:relational@db.relational-data.org/stats")
pd.read_sql('SELECT COUNT(*) FROM posts', engine)

def query(sql):
    return pd.read_sql(sql, engine)
stats_query = """
SELECT
    COUNT(*) as n,
    AVG(Age) as avg_age,
    AVG(Reputation) as avg_reputation,
    SUM(Age * Reputation) as sum_age_reputation,
    SUM(Age * Age) as sum_age_age,
    SUM(Reputation * Reputation) as sum_reputation_reputation
FROM
    users
WHERE
    Age IS NOT NULL AND Reputation IS NOT NULL
"""

stats = query(stats_query)

# manual calculation of pearson correlation
# Extract the aggregated values from the DataFrame
n = stats["n"].iloc[0]
avg_age = stats["avg_age"].iloc[0]
avg_reputation = stats["avg_reputation"].iloc[0]
sum_age_reputation = stats["sum_age_reputation"].iloc[0]
sum_age_age = stats["sum_age_age"].iloc[0]
sum_reputation_reputation = stats["sum_reputation_reputation"].iloc[0]

# Calculate the Pearson correlation coefficient
numerator = sum_age_reputation - n * avg_age * avg_reputation
denominator = np.sqrt(
    (sum_age_age - n * avg_age**2) * (sum_reputation_reputation - n * avg_reputation**2)
)

if denominator != 0:
    pearson_correlation = numerator / denominator
else:
    pearson_correlation = np.nan  # Handle division by zero if it occurs

print(f"Pearson correlation coefficient: {pearson_correlation}")
```

- **SQL is a ANALYTICS tool too**

- SQLite is a database-in-a-file. If you get a SQLite database file (e.g. data.db), you can connect to it using the SQLAlchemy string:
```python
# Assume data.db is in the current directory and has a table named "tablename"
engine = sa.create_engine("sqlite:///data.db/tablename")
```
---

Refrences:
1. [forecasting in python](https://youtu.be/aedA2javxvE?si=lroTS8CKSInEAARg)

2. [the parquet dataset used in the python section](https://drive.google.com/file/d/1XGvuFjoTwlybkw0cc9u34horMF9vMhrB/view)