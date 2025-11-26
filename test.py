
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
print("\n1. DATA GENERATION    -------------------------------------------------------------")

def generate_random_sales(mn, mx, size):

    random_sales = []
    for _ in range(size):
        random_sales.append(random.randint(mn, mx))

    return random_sales

months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

print("\nOne possibility is to have the indexes be the months as following:")
data = {
    'Product A': generate_random_sales(50, 100, 12),
    'Product B': generate_random_sales(30, 80, 12),
    'Product C': generate_random_sales(20, 60, 12),
    'Product D': generate_random_sales(10, 50, 12),
}
df = pd.DataFrame(data, index=pd.Index(months))
print(f"\n{df}")

print("\nOr we could have the months be a column of their own and instead use pandas's defautl indexing:")
data = {
    'Month': months,
    'Product A': generate_random_sales(50, 100, 12),
    'Product B': generate_random_sales(30, 80, 12),
    'Product C': generate_random_sales(20, 60, 12),
    'Product D': generate_random_sales(10, 50, 12),
}
df = pd.DataFrame(data)
print(f"\n{df}")

print("\nwe won't use the months as indexes. It wasn't specified in the assignment so we'll stick to pandas's defaults")
df.to_csv("data/initial.csv")

print("\n2. FINAL DATA FRAME         -------------------------------------------------------------")

# there 3 main ways to access data frames:
#
#    - df['some column']                     .-> returns a pandas series (pandas.core.series.Series)
#                                            .-> it's an indexed (labeled) array
#
#    - df[['some column']]                   .-> returns a data frame with one column 'some column'
#
#    - df[['some column', 'other column']]   .-> it works for multiple columns
#
#    - df.loc[0]     .-> returns the line number 0 as a series with the corresponding column name for
#                    .-> each label (index). Here '0' just happens to be the default index in
#                    .-> data frames. If we had set 'months' to be the indexes then we would have said
#                    .-> df.loc['JAN'] instead to get the first line
#

# 2.1 Total Sales: performs addition based on the indexes (axis labels)
df['Total Sales'] = df['Product A'] + df['Product B'] + df['Product C'] + df['Product D']

# 2.2 Averate Sales
# .mean() creates a pandas series with the mean of the data frame
# axis=1 -> rows
# axis=0 -> columns
df['Average Sales'] = df[['Product B', 'Product A', 'Product C', 'Product D']].mean(axis=1)

# 2.3 Month Over Month Growth

# Manual solution

prev = 0
growth = []
for total_sales in df['Total Sales']:
    if prev != 0:
        change = (total_sales - prev) / prev * 100
        growth.append("{:.2f}%".format(change))
    else:
        growth.append("100%")
    prev = total_sales

df['Month over Month Growth'] = growth

# Pandas's solution

# pct_change() returns a pandas series with the step-by-step change rate for each entry of the given series
df['Month over Month Growth'] = df['Total Sales'] \
                                    .pct_change() \
                                    .apply(lambda x : "{:.2f}%".format(x*100 if not np.isnan(x) else 100))

# 2.4 Quarters

month_quarter = {
    "JAN": "Q1",
    "FEB": "Q1",
    "MAR": "Q1",
    "APR": "Q2",
    "MAY": "Q2",
    "JUN": "Q2",
    "JUL": "Q3",
    "AUG": "Q3",
    "SEP": "Q3",
    "OCT": "Q4",
    "NOV": "Q4",
    "DEC": "Q4",
}

# .map() would work just fine but it would make my type-checker complain
df['Quarter'] = df['Month'].replace(month_quarter)

# 2.5 Min & Max sold products
df['Min Sales Product'] = df[['Product A', 'Product B', 'Product C', 'Product D']].idxmin(axis=1)
df['Max Sales Product'] = df[['Product A', 'Product B', 'Product C', 'Product D']].idxmax(axis=1)

df.to_csv('data/final.csv')
print(f"\n{df}")

print("\n3. PIVOT TABLES & SUMMARIES -------------------------------------------------------------")

print("""\n
Pivot tables are used when you want to aggegate multiple values of two differenct columns
here we only have one column that we want to groub by and it's 'Quarter'. For the products A, B, C, and D
they are already separated therefore do not require that we pivot arround them. So a group by is enough
""")

per_quarter = df.groupby('Quarter')
average_sales_per_product_per_quarter = round(per_quarter[["Product A", "Product B", "Product C", "Product D"]].mean(), 2)
total_sales_per_quarter = per_quarter['Total Sales'].sum()
print(f"\naverage_sales_per_product_per_quarter:\n\n{average_sales_per_product_per_quarter}")
print(f"\ntotal_sales_per_quarter:\n\n{total_sales_per_quarter}")

average_sales_per_product_per_quarter.to_csv("data/average_sales_per_product_per_quarter.csv")
total_sales_per_quarter.to_csv("data/total_sales_per_quarter.csv")

print("\n4. INSIGHTS -------------------------------------------------------------")

# Here the axis parameter is unused since a series is 1-dimensional
max_total_sales_index = df['Total Sales'].idxmax()
max_total_sales_row = df.loc[max_total_sales_index]
month = max_total_sales_row['Month']
print(f"\nBest Month in total sales: {month}")

# it will sum with axis=0 (columns) by default. So we'll have 4 values, one for each product (a series)
per_product_annual_sales = df[['Product A', 'Product B', 'Product C', 'Product D']].sum()
max_yearly_sales_product = per_product_annual_sales.idxmax()
print(f"\nAnnual Sales: \n{per_product_annual_sales}")
print(f"\nBest produt in annual sales: {max_yearly_sales_product}")

# we'll reuse the groupby we made for Q3
print(f"\nTotal Sales per Quarter:\n\n{total_sales_per_quarter}")
print(f"\nBest quarter in total sales: {total_sales_per_quarter.idxmax()}")
