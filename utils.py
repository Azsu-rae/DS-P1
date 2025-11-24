
import pandas as pd
import numpy as np
import random

def generate_random_sales(mn, mx, size):

    values = []
    for _ in range(size):
        values.append(random.randint(mn, mx))

    return np.array(values)

months = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]

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
