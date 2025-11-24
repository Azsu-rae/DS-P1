
import utils as ut

import pandas as pd

sales = {
    'Month': ut.months,
    'Product A': ut.generate_random_sales(50, 100, 12),
    'Product B': ut.generate_random_sales(30, 80, 12),
    'Product C': ut.generate_random_sales(20, 60, 12),
    'Product D': ut.generate_random_sales(10, 50, 12),
}

df = pd.DataFrame(sales)

df.to_csv("data/initial.csv")

df['Total Sales'] = df['Product A'] + df['Product B'] + df['Product C'] + df['Product D']

df['Average Sales'] = df[['Product A', 'Product B', 'Product C', 'Product D']].mean(axis=1)

print(df['Total Sales'])
