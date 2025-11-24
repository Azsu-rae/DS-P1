
import pandas as pd
import numpy as np
import utils

# 1. DATA GENERATION    -------------------------------------------------------------

sales = {
    'Month': utils.months,
    'Product A': utils.generate_random_sales(50, 100, 12),
    'Product B': utils.generate_random_sales(30, 80, 12),
    'Product C': utils.generate_random_sales(20, 60, 12),
    'Product D': utils.generate_random_sales(10, 50, 12),
}

# 'months' is an array defined in the utils.py module
# all arrays/disctionaries are defined there to avoid crowding this solution

df = pd.DataFrame(sales)
df.to_csv("data/initial.csv")

# 2. DATA FRAME         -------------------------------------------------------------

# 2.1 Total Sales

df['Total Sales'] = df['Product A'] + df['Product B'] + df['Product C'] + df['Product D']

# 2.2 Averate Sales

# there 2 main ways to access data in pandas:
#   - df['some column']     -> returns a pandas series (pandas.core.series.Series)
#   - df[['some column']]   -> returns a data frame with one column 'some column'
#
# you can use the double [] to create new data frames based on existing ones

# .mean() creates a pandas series with the mean of the data frame
# axis = 1 -> mean of the lines
# axis = 0 -> mean of the columns

df['Average Sales'] = df[['Product B', 'Product A', 'Product C', 'Product D']].mean(axis=1)

# 2.3 Month_Over_Month_Growth

# Manual solution

prev = 0
growth = []
for total_sales in df['Total Sales']:
    if prev != 0:
        growth.append(f"{round(((total_sales - prev) / prev) * 100, 2)}%")
    else:
        growth.append("100%")
    prev = total_sales

df['Month over Month Growth'] = growth

# Pandas's solution

df['Month over Month Growth'] = df['Total Sales'].pct_change().apply(lambda x : f"{round(x*100, 2) if not np.isnan(x) else 100}%")

# 2.4 Quarters

df['Quarter'] = df['Month'].map(utils.month_quarter)

# 2.5 Min & Max sold products

df['Min Sales Product'] = df[['Product A', 'Product B', 'Product C', 'Product D']].idxmin(axis=1)
df['Max Sales Product'] = df[['Product A', 'Product B', 'Product C', 'Product D']].idxmax(axis=1)

df.to_csv('data/final.csv')

print(df)
