# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:09:44 2023

@author: lEO
"""

import warnings
import matplotlib.pyplot as plt
from DataPreprocessing import all_transaction

warnings.filterwarnings("ignore")

    
# Visualizing Sales Made each day across different members.
for date, sales in all_transaction.items():
    people = []
    purchases = []
    for user, item in sales.items():
        people.append(str(user))
        purchases.append(len(item))
    
    plt.figure(figsize = (15, 10))
    plt.title(f"Total transactions made by customers on {date}")
    plt.bar(x = people, height = purchases, width = 0.5, label = people, color = "brown")
    plt.xlabel("Member number")
    plt.ylabel("Number of purchases made")
    plt.show()

