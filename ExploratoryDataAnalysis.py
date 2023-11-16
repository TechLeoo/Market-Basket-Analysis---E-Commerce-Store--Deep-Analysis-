# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:10:19 2023

@author: lEO
"""

import warnings
import pandas as pd
from DataPreprocessing import dataset, data2014, data2015

# Exploratory Data Analysis (EDA 2014 to 2015)
warnings.filterwarnings("ignore")

# EDA
dataset.info()
data_head = dataset.head()
data_tail = dataset.tail()

        # (1) EDA (Items Purchased 2014 to 2015)
data_item_value_counts = dataset.itemDescription.value_counts().reset_index()
data_item_value_counts.rename(columns = {"index": "Items", "itemDescription": "Number of Item Purchases 2014 - 2015"}, inplace = True)
item_purchase_head = data_item_value_counts.head()
item_purchase_tail = data_item_value_counts.tail()
item_purchase_descriptive_statistics = data_item_value_counts.describe()
item_purchase_histogram = data_item_value_counts.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
item_purchase_mean = data_item_value_counts["Number of Item Purchases 2014 - 2015"].mean()
item_purchase_median = data_item_value_counts["Number of Item Purchases 2014 - 2015"].median()
item_purchase_mode = data_item_value_counts["Number of Item Purchases 2014 - 2015"].mode()[0]
item_purchase_standard_deviation = data_item_value_counts["Number of Item Purchases 2014 - 2015"].std()
item_purchase_variance = data_item_value_counts["Number of Item Purchases 2014 - 2015"].var()
item_purchase_range = data_item_value_counts["Number of Item Purchases 2014 - 2015"].max() - data_item_value_counts["Number of Item Purchases 2014 - 2015"].min()


        # (2) EDA (Member Purchases 2014 to 2015)
data_count_member_purchase = dataset.Member_number.value_counts().reset_index()
data_count_member_purchase.rename(columns = {"index": "Member Number", "Member_number": "Number of Purchases Made by Members 2014 - 2015"}, inplace = True)
data_count_member_purchase["Member Number"] = data_count_member_purchase["Member Number"].astype(object)
member_purchase_head = data_count_member_purchase.head()
member_purchase_tail = data_count_member_purchase.tail()
member_purchase_descriptive_statistics = data_count_member_purchase.describe()
member_purchase_histogram = data_count_member_purchase.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
member_purchase_mean = data_count_member_purchase["Number of Purchases Made by Members 2014 - 2015"].mean()
member_purchase_median = data_count_member_purchase["Number of Purchases Made by Members 2014 - 2015"].median()
member_purchase_mode = data_count_member_purchase["Number of Purchases Made by Members 2014 - 2015"].mode()[0]
member_purchase_standard_deviation = data_count_member_purchase["Number of Purchases Made by Members 2014 - 2015"].std()
member_purchase_variance = data_count_member_purchase["Number of Purchases Made by Members 2014 - 2015"].var()
member_purchase_range = data_count_member_purchase["Number of Purchases Made by Members 2014 - 2015"].max() - data_count_member_purchase["Number of Purchases Made by Members 2014 - 2015"].min()


        # (3) EDA (Number of Transactions on Each Day... 2014 to 2015)
data_purchase_date_count = dataset.Date.value_counts().reset_index()
data_purchase_date_count.rename(columns = {"index": "Date", "Date": "Purchases Made by Members on different dates between 2014 - 2015"}, inplace = True)
data_purchase_date_count["Date"] = pd.to_datetime(data_purchase_date_count.loc[:, "Date"])
count_date_purchase_head = data_purchase_date_count.head()
count_date_purchase_tail = data_purchase_date_count.tail()
count_date_purchase_descriptive_statistics = data_purchase_date_count.describe()
count_date_purchase_histogram = data_purchase_date_count.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
count_date_purchase_mean = data_purchase_date_count["Purchases Made by Members on different dates between 2014 - 2015"].mean()
count_date_purchase_median = data_purchase_date_count["Purchases Made by Members on different dates between 2014 - 2015"].median()
count_date_purchase_mode = data_purchase_date_count["Purchases Made by Members on different dates between 2014 - 2015"].mode()[0]
count_date_purchase_standard_deviation = data_purchase_date_count["Purchases Made by Members on different dates between 2014 - 2015"].std()
count_date_purchase_variance = data_purchase_date_count["Purchases Made by Members on different dates between 2014 - 2015"].var()
count_date_purchase_range = data_purchase_date_count["Purchases Made by Members on different dates between 2014 - 2015"].max() - data_purchase_date_count["Purchases Made by Members on different dates between 2014 - 2015"].min()




# Exploratory Data Analysis (EDA 2014)
dataset2014 = data2014
dataset2014["Member_number"] = data2014["Member_number"].astype(object)

# EDA
dataset2014.info()
data_head2014 = dataset2014.head()
data_tail2014 = dataset2014.tail()

        # (1) EDA (Items Purchased 2014)
data_item_value_counts2014 = dataset2014.itemDescription.value_counts().reset_index()
data_item_value_counts2014.rename(columns = {"index": "Items", "itemDescription": "Number of Item Purchases in 2014"}, inplace = True)
item_purchase2014_head = data_item_value_counts2014.head()
item_purchase2014_tail = data_item_value_counts2014.tail()
item_purchase2014_descriptive_statistics = data_item_value_counts2014.describe()
item_purchase2014_histogram = data_item_value_counts2014.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
item_purchase_mean2014 = data_item_value_counts2014["Number of Item Purchases in 2014"].mean()
item_purchase_median2014 = data_item_value_counts2014["Number of Item Purchases in 2014"].median()
item_purchase_mode2014 = data_item_value_counts2014["Number of Item Purchases in 2014"].mode()[0]
item_purchase_standard_deviation2014 = data_item_value_counts2014["Number of Item Purchases in 2014"].std()
item_purchase_variance2014 = data_item_value_counts2014["Number of Item Purchases in 2014"].var()
item_purchase_range2014 = data_item_value_counts2014["Number of Item Purchases in 2014"].max() - data_item_value_counts2014["Number of Item Purchases in 2014"].min()


        # (2) EDA (Member Purchases 2014) 
data_count_member_purchase2014 = dataset2014.Member_number.value_counts().reset_index()
data_count_member_purchase2014.rename(columns = {"index": "Member Number", "Member_number": "Number of Purchases Made by Members in 2014"}, inplace = True)
data_count_member_purchase2014["Member Number"] = data_count_member_purchase2014["Member Number"].astype(object)
member_purchase2014_head = data_count_member_purchase2014.head()
member_purchase2014_tail = data_count_member_purchase2014.tail()
member_purchase2014_descriptive_statistics = data_count_member_purchase2014.describe()
member_purchase2014_histogram = data_count_member_purchase2014.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
member_purchase_mean2014 = data_count_member_purchase2014["Number of Purchases Made by Members in 2014"].mean()
member_purchase_median2014 = data_count_member_purchase2014["Number of Purchases Made by Members in 2014"].median()
member_purchase_mode2014 = data_count_member_purchase2014["Number of Purchases Made by Members in 2014"].mode()[0]
member_purchase_standard_deviation2014 = data_count_member_purchase2014["Number of Purchases Made by Members in 2014"].std()
member_purchase_variance2014 = data_count_member_purchase2014["Number of Purchases Made by Members in 2014"].var()
member_purchase_range2014 = data_count_member_purchase2014["Number of Purchases Made by Members in 2014"].max() - data_count_member_purchase2014["Number of Purchases Made by Members in 2014"].min()


        # (3) EDA (Number of Transactions on Each Day... 2014)
data_purchase_date_count2014 = dataset2014.Date.value_counts().reset_index()
data_purchase_date_count2014.rename(columns = {"index": "Date", "Date": "Purchases Made by Members on different dates in 2014"}, inplace = True)
data_purchase_date_count2014["Date"] = pd.to_datetime(data_purchase_date_count2014.loc[:, "Date"])
count_date_purchase_head2014 = data_purchase_date_count2014.head()
count_date_purchase_tail2014 = data_purchase_date_count2014.tail()
count_date_purchase_descriptive_statistics2014 = data_purchase_date_count2014.describe()
count_date_purchase_histogram2014 = data_purchase_date_count2014.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
count_date_purchase_mean2014 = data_purchase_date_count2014["Purchases Made by Members on different dates in 2014"].mean()
count_date_purchase_median2014 = data_purchase_date_count2014["Purchases Made by Members on different dates in 2014"].median()
count_date_purchase_mode2014 = data_purchase_date_count2014["Purchases Made by Members on different dates in 2014"].mode()[0]
count_date_purchase_standard_deviation2014 = data_purchase_date_count2014["Purchases Made by Members on different dates in 2014"].std()
count_date_purchase_variance2014 = data_purchase_date_count2014["Purchases Made by Members on different dates in 2014"].var()
count_date_purchase_range2014 = data_purchase_date_count2014["Purchases Made by Members on different dates in 2014"].max() - data_purchase_date_count2014["Purchases Made by Members on different dates in 2014"].min()





# Exploratory Data Analysis (EDA 2015)
dataset2015 = data2015
dataset2015["Member_number"] = data2015["Member_number"].astype(object)


# EDA
dataset2015.info()
data_head2015 = dataset2015.head()
data_tail2015 = dataset2015.tail()

        # (1) EDA (Items Purchased 2015)
data_item_value_counts2015 = dataset2015.itemDescription.value_counts().reset_index()
data_item_value_counts2015.rename(columns = {"index": "Items", "itemDescription": "Number of Item Purchases in 2015"}, inplace = True)
item_purchase2015_head = data_item_value_counts2015.head()
item_purchase2015_tail = data_item_value_counts2015.tail()
item_purchase2015_descriptive_statistics = data_item_value_counts2015.describe()
item_purchase2015_histogram = data_item_value_counts2015.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
item_purchase_mean2015 = data_item_value_counts2015["Number of Item Purchases in 2015"].mean()
item_purchase_median2015 = data_item_value_counts2015["Number of Item Purchases in 2015"].median()
item_purchase_mode2015 = data_item_value_counts2015["Number of Item Purchases in 2015"].mode()[0]
item_purchase_standard_deviation2015 = data_item_value_counts2015["Number of Item Purchases in 2015"].std()
item_purchase_variance2015 = data_item_value_counts2015["Number of Item Purchases in 2015"].var()
item_purchase_range2015 = data_item_value_counts2015["Number of Item Purchases in 2015"].max() - data_item_value_counts2015["Number of Item Purchases in 2015"].min()


        # (2) EDA (Member Purchases 2015)
data_count_member_purchase2015 = dataset2015.Member_number.value_counts().reset_index()
data_count_member_purchase2015.rename(columns = {"index": "Member Number", "Member_number": "Number of Purchases Made by Members in 2015"}, inplace = True)
data_count_member_purchase2015["Member Number"] = data_count_member_purchase2015["Member Number"].astype(object)
member_purchase2015_head = data_count_member_purchase2015.head()
member_purchase2015_tail = data_count_member_purchase2015.tail()
member_purchase2015_descriptive_statistics = data_count_member_purchase2015.describe()
member_purchase2015_histogram = data_count_member_purchase2015.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
member_purchase_mean2015 = data_count_member_purchase2015["Number of Purchases Made by Members in 2015"].mean()
member_purchase_median2015 = data_count_member_purchase2015["Number of Purchases Made by Members in 2015"].median()
member_purchase_mode2015 = data_count_member_purchase2015["Number of Purchases Made by Members in 2015"].mode()[0]
member_purchase_standard_deviation2015 = data_count_member_purchase2015["Number of Purchases Made by Members in 2015"].std()
member_purchase_variance2015 = data_count_member_purchase2015["Number of Purchases Made by Members in 2015"].var()
member_purchase_range2015 = data_count_member_purchase2015["Number of Purchases Made by Members in 2015"].max() - data_count_member_purchase2015["Number of Purchases Made by Members in 2015"].min()


        # (3) EDA (Number of Transactions on Each Day... 2015)
data_purchase_date_count2015 = dataset2015.Date.value_counts().reset_index()
data_purchase_date_count2015.rename(columns = {"index": "Date", "Date": "Purchases Made by Members on different dates in 2015"}, inplace = True)
data_purchase_date_count2015["Date"] = pd.to_datetime(data_purchase_date_count2015.loc[:, "Date"])
count_date_purchase_head2015 = data_purchase_date_count2015.head()
count_date_purchase_tail2015 = data_purchase_date_count2015.tail()
count_date_purchase_descriptive_statistics2015 = data_purchase_date_count2015.describe()
count_date_purchase_histogram2015 = data_purchase_date_count2015.hist(figsize = (15, 10), bins = 10)
                # ----> Basic Statistics
count_date_purchase_mean2015 = data_purchase_date_count2015["Purchases Made by Members on different dates in 2015"].mean()
count_date_purchase_median2015 = data_purchase_date_count2015["Purchases Made by Members on different dates in 2015"].median()
count_date_purchase_mode2015 = data_purchase_date_count2015["Purchases Made by Members on different dates in 2015"].mode()[0]
count_date_purchase_standard_deviation2015 = data_purchase_date_count2015["Purchases Made by Members on different dates in 2015"].std()
count_date_purchase_variance2015 = data_purchase_date_count2015["Purchases Made by Members on different dates in 2015"].var()
count_date_purchase_range2015 = data_purchase_date_count2015["Purchases Made by Members on different dates in 2015"].max() - data_purchase_date_count2015["Purchases Made by Members on different dates in 2015"].min()













































