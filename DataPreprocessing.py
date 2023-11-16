# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:04:46 2023

@author: lEO
"""

import warnings
import pandas as pd
from datetime import datetime, timedelta
from mlxtend.preprocessing import TransactionEncoder

warnings.filterwarnings("ignore")
dataset = pd.read_csv("Market Basket Analysis - Groceries_dataset.csv")

# STEP 1: Create a list of the days transactions were made.
# STEP 2: Create a list of items that were bought together by a customer on that day.


# CREATING A LIST OF TRANSACTIONS
# ---> Fixing the DATE COLUMN
dataset["Date"] = pd.to_datetime(dataset["Date"], dayfirst = True,)
dataset.info()

# ---> Fixing the MEMBER COLUMN
dataset["Member_number"] = dataset["Member_number"].astype(object)

# ---> 2015 Dataset
data2015 = dataset[(dataset["Date"] < datetime(2016, 1, 1)) & (dataset["Date"] >= datetime(2015, 1, 1))]
data2015["Member_number"] = data2015["Member_number"].astype(object)

# ---> 2014 Dataset
data2014 = dataset[dataset["Date"] < datetime(2015, 1, 1)]
data2014["Member_number"] = data2014["Member_number"].astype(object)





# ----> Grouping by Customers for Each Day
date = datetime(2014, 1, 1)

all_transaction = {}
count = 1
while date < datetime(2016, 1, 1):
    data1 = dataset[dataset["Date"] == date]
    transaction = {}
    numbers = []
    for number, desc in zip(data1.iloc[:, 0], data1.iloc[:, 2]):
        if number not in numbers:
            numbers.append(number)
            transaction[number] = []
            transaction[number].append(desc)
        else:
            transaction[number].append(desc)
           
    # print(transaction)     
    all_transaction[f"{date}"] = transaction
    date = date + timedelta(days = 1)
    # print(date)



List_Total_Transactions = []
a = list(all_transaction.values())
for number in range(0, 730):
    for key, value in a[number].items():
        List_Total_Transactions.append(value)
        




# ----> Grouping by Customers for Each Day 2014
date1 = datetime(2014, 1, 1)

all_transaction2014 = {}
count = 1
while date1 < datetime(2015, 1, 1):
    data2 = dataset[dataset["Date"] == date1]
    transaction1 = {}
    numbers1 = []
    for number, desc in zip(data2.iloc[:, 0], data2.iloc[:, 2]):
        if number not in numbers:
            numbers1.append(number)
            transaction1[number] = []
            transaction1[number].append(desc)
        else:
            transaction1[number].append(desc)
           
    # print(transaction)     
    all_transaction2014[f"{date1}"] = transaction1
    date1 = date1 + timedelta(days = 1)
    # print(date)



List_Total_Transactions2014 = []
b = list(all_transaction2014.values())
for number1 in range(0, 365):
    for key, value in b[number1].items():
        List_Total_Transactions2014.append(value)
      
        
      
        
      
# ----> Grouping by Customers for Each Day 2015
date2 = datetime(2015, 1, 1)

all_transaction2015 = {}
count = 1
while date2 < datetime(2016, 1, 1):
    data3 = dataset[dataset["Date"] == date2]
    transaction2 = {}
    numbers2 = []
    for number, desc in zip(data3.iloc[:, 0], data3.iloc[:, 2]):
        if number not in numbers:
            numbers2.append(number)
            transaction2[number] = []
            transaction2[number].append(desc)
        else:
            transaction2[number].append(desc)
           
    # print(transaction2)     
    all_transaction2015[f"{date2}"] = transaction2
    date2 = date2 + timedelta(days = 1)
    # print(date2)



List_Total_Transactions2015 = []
c = list(all_transaction2015.values())
for number2 in range(0, 365):
    for key, value in b[number2].items():
        List_Total_Transactions2015.append(value)





# ----> ENCODING THE DATA 2014 to 2015
transaction = List_Total_Transactions

encoder = TransactionEncoder()
transactionData = encoder.fit_transform(transaction)
EncodedDatasetAssociationRule = pd.DataFrame(transactionData, columns = encoder.columns_)


# ----> ENCODING THE DATA 2014
transaction2014 = List_Total_Transactions2014

encoder2014 = TransactionEncoder()
transactionData2014 = encoder2014.fit_transform(transaction2014)
EncodedDatasetAssociationRule2014 = pd.DataFrame(transactionData2014, columns = encoder2014.columns_)


# ----> ENCODING THE DATA 2015
transaction2015 = List_Total_Transactions2015

encoder2015 = TransactionEncoder()
transactionData2015 = encoder2015.fit_transform(transaction2015)
EncodedDatasetAssociationRule2015 = pd.DataFrame(transactionData2015, columns = encoder2015.columns_)



# -------> Save the Encoded Datasets to File
EncodedDatasetAssociationRule.to_csv(r"EncodedDatasets - Association Rule\Encodeddata2014to2015.csv", index = True)
EncodedDatasetAssociationRule2014.to_csv(r"EncodedDatasets - Association Rule\Encodeddata2014.csv", index = True)
EncodedDatasetAssociationRule2015.to_csv(r"EncodedDatasets - Association Rule\Encodeddata2015.csv", index = True)