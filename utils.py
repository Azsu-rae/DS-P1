
import pandas as pd
import numpy as np
import random

def generate_random_sales(mn, mx, size):

    values = []
    for _ in range(size):
        values.append(random.randint(mn, mx))

    return np.array(values)

dates = [
    ('2025-01-01', '2025-01-31'),
    ('2025-02-01', '2025-02-28'),
    ('2025-03-01', '2025-03-31'),
    ('2025-04-01', '2025-04-30'),
    ('2025-05-01', '2025-05-31'),
    ('2025-06-01', '2025-06-30'),
    ('2025-07-01', '2025-07-31'),
    ('2025-08-01', '2025-08-31'),
    ('2025-09-01', '2025-09-30'),
    ('2025-10-01', '2025-10-31'),
    ('2025-11-01', '2025-11-30'),
    ('2025-12-01', '2025-12-31'),
]

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
