# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:24:45 2023

@author: lEO
"""
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from DataPreprocessing import dataset, all_transaction

warnings.filterwarnings("ignore")

# 1) Graph of item purchased.
item_count = {}
food = []
for foodstuff in dataset.itemDescription:
    if foodstuff not in food:
        food.append(foodstuff)
        item_count[foodstuff] = 1
    else:
        item_count[foodstuff] += 1

itemstoplot = []
countofitems = []
for item, count in item_count.items():
    itemstoplot.append(item)
    countofitems.append(count)

datacountforitem = pd.DataFrame({"FoodItems": itemstoplot, "NumberPurchased": countofitems}).sort_values(by = "NumberPurchased", ascending = True)
        
        # (a) Items purchased the most
top20itemspurchased = datacountforitem.iloc[-21:, :]

plt.figure(figsize = (15, 15))
plt.title("Top 20 items purchased")
bar = plt.barh(y = top20itemspurchased.iloc[:, 0], width = top20itemspurchased.iloc[:, 1], height = 0.5, color = "brown")
plt.bar_label(container = bar, labels = top20itemspurchased.iloc[:, 1], padding = 5)
plt.ylabel("Items")
plt.xlabel("Number of purchases made")
plt.show()
        
        # (b) Least purchased items
top20leastpurchased = datacountforitem.iloc[:20, :]

plt.figure(figsize = (15, 15))
plt.title("Least 20 items purchased")
bar = plt.barh(y = top20leastpurchased.iloc[:, 0], width = top20leastpurchased.iloc[:, 1], height = 0.5, color = "brown")
plt.bar_label(container = bar, labels = top20leastpurchased.iloc[:, 1], padding = 5)
plt.ylabel("Items")
plt.xlabel("Number of purchases made")
plt.show()



# 2) Sales across different Times in the data
date_format = '%Y-%m-%d %H:%M:%S'
Sales = {}

# ----> SALES MADE EACH YEAR
for sale, purchase in all_transaction.items():
    Sales[sale] = 0
    for member, bought in purchase.items():
        num_items_bought = len(bought)
        Sales[sale] += num_items_bought

        # (a) Yearly Sales
Year2014 = 0
Year2015 = 0
for timecheck, items_purchased in Sales.items():
    timecheck = datetime.strptime(timecheck, date_format)
    if timecheck.year == 2014:
        Year2014 += items_purchased
    elif timecheck.year == 2015:
        Year2015 += items_purchased
    
plt.figure(figsize = (10, 10))
plt.title("Yearly Sales")
bar = plt.bar(x = ["2014", "2015"], height = [Year2014, Year2015], width = 0.5, color = "brown")
plt.bar_label(container = bar, labels = [Year2014, Year2015], padding = 5)
plt.ylabel("Items")
plt.xlabel("Number of purchases made")
plt.show()  

        # (b) - i) Monthly Sales 2014
date_format = '%Y-%m-%d %H:%M:%S'
monthlysales2014 = {"Jan-2014": 0, "Feb-2014": 0, "Mar-2014": 0, "Apr-2014": 0, "May-2014": 0, "Jun-2014": 0, "Jul-2014": 0, "Aug-2014": 0, "Sep-2014": 0, "Oct-2014": 0, "Nov-2014": 0, "Dec-2014": 0}  

for checktime, purchased_item in Sales.items():
    checktime = datetime.strptime(checktime, date_format)
    if checktime.month == 1 and checktime.year == 2014:
        monthlysales2014["Jan-2014"] = monthlysales2014["Jan-2014"] + purchased_item
    elif checktime.month == 2 and checktime.year == 2014:
        monthlysales2014["Feb-2014"] = monthlysales2014["Feb-2014"] + purchased_item
    elif checktime.month == 3 and checktime.year == 2014:
        monthlysales2014["Mar-2014"] = monthlysales2014["Mar-2014"] + purchased_item
    elif checktime.month == 4 and checktime.year == 2014:
        monthlysales2014["Apr-2014"] = monthlysales2014["Apr-2014"] + purchased_item
    elif checktime.month == 5 and checktime.year == 2014:
        monthlysales2014["May-2014"] = monthlysales2014["May-2014"] + purchased_item
    elif checktime.month == 6 and checktime.year == 2014:
        monthlysales2014["Jun-2014"] = monthlysales2014["Jun-2014"] + purchased_item
    elif checktime.month == 7 and checktime.year == 2014:
        monthlysales2014["Jul-2014"] = monthlysales2014["Jul-2014"] + purchased_item
    elif checktime.month == 8 and checktime.year == 2014:
        monthlysales2014["Aug-2014"] = monthlysales2014["Aug-2014"] + purchased_item
    elif checktime.month == 9 and checktime.year == 2014:
        monthlysales2014["Sep-2014"] = monthlysales2014["Sep-2014"] + purchased_item
    elif checktime.month == 10 and checktime.year == 2014:
        monthlysales2014["Oct-2014"] = monthlysales2014["Oct-2014"] + purchased_item
    elif checktime.month == 11 and checktime.year == 2014:
        monthlysales2014["Nov-2014"] = monthlysales2014["Nov-2014"] + purchased_item
    elif checktime.month == 12 and checktime.year == 2014:
        monthlysales2014["Dec-2014"] = monthlysales2014["Dec-2014"] + purchased_item

month2014 = [month for month in monthlysales2014.keys()]   
monthSales = [sale for sale in monthlysales2014.values()] 
monthlysalesdata2014 = pd.DataFrame({"Month": month2014, "Sales": monthSales})  
    
plt.figure(figsize = (20, 10))
plt.title("Deep View on 2014 Monthly Sales", pad = 10)
plt.plot(month2014, monthSales, 'go--', linestyle = 'dashed', marker = 'o', markersize = 12)
for x1, y1 in zip(monthlysalesdata2014.Month, monthlysalesdata2014.Sales):
    plt.text(x = x1, y = y1 + 5, s = str(y1), horizontalalignment = "center", verticalalignment = "bottom", size = "large", fontweight = 80, fontstretch = 50)
plt.xlabel("Months", labelpad = 20)
plt.ylabel("Total Sales", labelpad = 20)
plt.show()

        # (b) - ii) Monthly Sales 2015
date_format = '%Y-%m-%d %H:%M:%S'
monthlysales2015 = {"Jan-2015": 0, "Feb-2015": 0, "Mar-2015": 0, "Apr-2015": 0, "May-2015": 0, "Jun-2015": 0, "Jul-2015": 0, "Aug-2015": 0, "Sep-2015": 0, "Oct-2015": 0, "Nov-2015": 0, "Dec-2015": 0}  

for checktime, purchased_item in Sales.items():
    checktime = datetime.strptime(checktime, date_format)
    if checktime.month == 1 and checktime.year == 2015:
        monthlysales2015["Jan-2015"] = monthlysales2015["Jan-2015"] + purchased_item
    elif checktime.month == 2 and checktime.year == 2015:
        monthlysales2015["Feb-2015"] = monthlysales2015["Feb-2015"] + purchased_item
    elif checktime.month == 3 and checktime.year == 2015:
        monthlysales2015["Mar-2015"] = monthlysales2015["Mar-2015"] + purchased_item
    elif checktime.month == 4 and checktime.year == 2015:
        monthlysales2015["Apr-2015"] = monthlysales2015["Apr-2015"] + purchased_item
    elif checktime.month == 5 and checktime.year == 2015:
        monthlysales2015["May-2015"] = monthlysales2015["May-2015"] + purchased_item
    elif checktime.month == 6 and checktime.year == 2015:
        monthlysales2015["Jun-2015"] = monthlysales2015["Jun-2015"] + purchased_item
    elif checktime.month == 7 and checktime.year == 2015:
        monthlysales2015["Jul-2015"] = monthlysales2015["Jul-2015"] + purchased_item
    elif checktime.month == 8 and checktime.year == 2015:
        monthlysales2015["Aug-2015"] = monthlysales2015["Aug-2015"] + purchased_item
    elif checktime.month == 9 and checktime.year == 2015:
        monthlysales2015["Sep-2015"] = monthlysales2015["Sep-2015"] + purchased_item
    elif checktime.month == 10 and checktime.year == 2015:
        monthlysales2015["Oct-2015"] = monthlysales2015["Oct-2015"] + purchased_item
    elif checktime.month == 11 and checktime.year == 2015:
        monthlysales2015["Nov-2015"] = monthlysales2015["Nov-2015"] + purchased_item
    elif checktime.month == 12 and checktime.year == 2015:
        monthlysales2015["Dec-2015"] = monthlysales2015["Dec-2015"] + purchased_item
        
month2015 = [month for month in monthlysales2015.keys()]   
salesmonth = [sale for sale in monthlysales2015.values()] 
monthlysalesdata2015 = pd.DataFrame({"Month": month2015, "Sales": salesmonth}) 

plt.figure(figsize = (20, 10))
plt.title("Deep View on 2015 Monthly Sales", pad = 10)
plt.plot(month2015, salesmonth, 'bo', linestyle = 'dashed', marker = 'o', markersize = 12)
for x2, y2 in zip(monthlysalesdata2015.Month, monthlysalesdata2015.Sales):
    plt.text(x2, y2 + 5, str(y2), horizontalalignment ='center', verticalalignment ='bottom', size = "large", fontweight = 80, fontstretch = 50)
plt.xlabel("Months", labelpad = 20)
plt.ylabel("Total Sales", labelpad = 20)
plt.show()

        # (c) - iii) Monthly Sales 2014 vs Monthly Sales 2015
plt.figure(figsize = (40, 10))

plt.subplot(121)
plt.plot(month2014, monthSales, color = "y", linestyle = 'dashed', marker = 'o', markersize = 12, markerfacecolor = "g",)
plt.title("2014 Monthly Sales", pad = 10)
for x3, y3 in zip(monthlysalesdata2014.Month, monthlysalesdata2014.Sales):
    plt.text(x3, y3 + 25, str(y3), horizontalalignment = "center", verticalalignment = "bottom", fontstretch = 50)
plt.yticks(np.arange(0, 2500, 150)) # Sets the scale for the Y-Axis

plt.subplot(122)
plt.plot(month2015, salesmonth, color = "c", linestyle = 'dashed', marker = 'o', markersize = 12, markerfacecolor = "b",)
plt.title("2015 Monthly Sales", pad = 10)
for x4, y4 in zip(monthlysalesdata2015.Month, monthlysalesdata2015.Sales):
    plt.text(x4, y4 + 25, str(y4), horizontalalignment = "center", verticalalignment = "bottom", fontstretch = 50)
plt.yticks(np.arange(0, 2500, 150)) # Sets the scale for the Y-Axis
plt.tight_layout()
plt.show()

        # (d) - iv) Graph of Monthly Sales between 2014 and 2015
                    # (1) Deep view analysis of changes
monthlysalesdata2014to2015 = pd.concat([monthlysalesdata2014, monthlysalesdata2015]) # Join two datasets across the ROWS

plt.figure(figsize = (40, 20))
plt.plot(monthlysalesdata2014to2015.Month, monthlysalesdata2014to2015.Sales, linestyle = "dashed", marker = "o", markersize = 12, color = 'c', markerfacecolor = 'b')
plt.title("Monthly Sales between January 2014 to December 2015 (Clearer view analysis of changes over time)", pad = 10)
for x5, y5 in zip(monthlysalesdata2014to2015.Month, monthlysalesdata2014to2015.Sales):
    plt.text(x5, y5 + 5, str(y5), horizontalalignment = "center", verticalalignment = "bottom", fontstretch = 50)
plt.xlabel("Months", labelpad = 20)
plt.ylabel("Number of items sold", labelpad = 20)
plt.show()


                    # (2) Adjusted for yaxis
monthlysalesdata2014to2015 = pd.concat([monthlysalesdata2014, monthlysalesdata2015])

plt.figure(figsize = (40, 20))
plt.plot(monthlysalesdata2014to2015.Month, monthlysalesdata2014to2015.Sales, linestyle = "dashed", marker = "o", markersize = 12, color = 'c', markerfacecolor = 'b')
plt.title("Monthly Sales between January 2014 to December 2015 (Monthly sales adjusted for proper scaling)", pad = 10)
for x5, y5 in zip(monthlysalesdata2014to2015.Month, monthlysalesdata2014to2015.Sales):
    plt.text(x5, y5 + 25, str(y5), horizontalalignment = "center", verticalalignment = "bottom", fontstretch = 50)
plt.yticks(np.arange(0, 2500, 150))
plt.xlabel("Months", labelpad = 20)
plt.ylabel("Number of items sold", labelpad = 20)
plt.show()

        # (e) Graph of number of people we sold/transactions to everyday (2014 - 2015)
date_of_purchase = [datetime.strptime(main, date_format).date() for main in all_transaction.keys()]
number_of_items = [len(bought) for bought in all_transaction.values()]
transactionyearlydata = pd.DataFrame({"Date": date_of_purchase, "Transactions": number_of_items})

plt.figure(figsize = (100, 20))
plt.title("Graph Analysis for Daily Transactions, 2014 to 2015", pad = 30, fontsize = 50)
plt.plot(date_of_purchase, number_of_items, 'bo', linestyle = 'dashed', marker = 'o', markersize = 5)
plt.xlabel("Months", labelpad = 20, fontsize = 50)
plt.ylabel("Number of Transactions", labelpad = 20, fontsize = 50)
plt.show()

        # (f) Graph of number of items sold eachday (2014 - 2015)
# 2014 and 2015 data
date_of_sales = [datetime.strptime(date_sold, date_format).date() for date_sold in Sales.keys()]
items_we_sold = [items_sold for items_sold in Sales.values()]
dailyitemsales2014to2015 = pd.DataFrame({"Date": date_of_sales, "ItemsSold": items_we_sold})

plt.figure(figsize = (100, 20))
plt.title("Graph Analysis for Items Sold Daily, 2014 to 2015", pad = 30, fontsize = 50)
plt.plot(date_of_sales, items_we_sold, 'bo', linestyle = 'dashed', marker = 'o', markersize = 5)
plt.xlabel("Months", labelpad = 20, fontsize = 50)
plt.ylabel("Number of items sold", labelpad = 20, fontsize = 50)
plt.show()

        # (g) Graph of number of items sold eachday in 2014
# 2014 data
date_of_sales2014 = []
items_we_sold2014 = []
for dateofsales, itemswesold in Sales.items():
    dateofsales = datetime.strptime(dateofsales, date_format).date()
    if dateofsales.year == 2014:
        date_of_sales2014.append(dateofsales)
        items_we_sold2014.append(itemswesold) 
dailyitemsales2014 = pd.DataFrame({"Date": date_of_sales2014, "ItemsSold": items_we_sold2014})

plt.figure(figsize = (100, 20))
plt.title("Graph Analysis for Items Sold Daily in 2014", pad = 30, fontsize = 50)
plt.plot(date_of_sales2014, items_we_sold2014, 'bo', linestyle = 'dashed', marker = 'o', markersize = 5)
plt.xlabel("Months in 2014", labelpad = 20, fontsize = 50)
plt.ylabel("Number of items sold", labelpad = 20, fontsize = 50)
plt.show()

        # (h) Graph of number of items sold eachday in 2015
# 2015 data
date_of_sales2015 = []
items_we_sold2015 = []
for salesdate, solditems in Sales.items():
    dateofsales = datetime.strptime(salesdate, date_format).date()
    if dateofsales.year == 2015:
        date_of_sales2015.append(salesdate)
        items_we_sold2015.append(solditems)
dailyitemsales2015 = pd.DataFrame({"Date": date_of_sales2015, "ItemsSold": items_we_sold2015})

plt.figure(figsize = (100, 20))
plt.title("Graph Analysis for Items Sold Daily in 2015", pad = 30, fontsize = 50)
plt.plot(date_of_sales2015, items_we_sold2015, 'bo', linestyle = 'dashed', marker = 'o', markersize = 5)
plt.xlabel("Months in 2015", labelpad = 20, fontsize = 50)
plt.ylabel("Number of items sold", labelpad = 20, fontsize = 50)
plt.show()


# 3) -- (a) Graph of member who purchased the most, 2014 to 2015
data_count_member_purchase = dataset.Member_number.value_counts().reset_index(name = "NumberPurchased")
data_count_member_purchase.rename(columns = {"index": "MemberNumber", "NumberPurchased": "NumberPurchased"}, inplace = True)
top25_data_count_member_purchase = data_count_member_purchase.iloc[:25, :].astype(object)

plt.figure(figsize = (40, 10))
plt.title("Graph of 25 highest ranking purchasing members, 2014 to 2015")
bar = plt.bar(x = [str(num) for num in top25_data_count_member_purchase.MemberNumber], height = [countpurchase for countpurchase in top25_data_count_member_purchase.NumberPurchased], width = 0.5, color = "brown")
plt.bar_label(container = bar, labels = top25_data_count_member_purchase.NumberPurchased, padding = 5)
plt.xlabel("Member Number")
plt.ylabel("Number of purchases made")
plt.show() 

    # -- (b) Graph of member who purchased the most in 2014
membernumber = []
dateregistered = []
for k, v in zip(dataset.Member_number, dataset.Date):
    if v.year == 2014:
        membernumber.append(k)
        dateregistered.append(v)

memberpurchases2014 = pd.DataFrame({"Date": dateregistered, "MemberNumber": membernumber})
memberpurchase2014count = memberpurchases2014.MemberNumber.value_counts().reset_index()
memberpurchase2014count.rename(columns = {"index": "MemberNumber", "MemberNumber": "NumberPurchased"}, inplace = True)
top20memberpurchase2014count = memberpurchase2014count.iloc[:20, :]

plt.figure(figsize = (40, 10))
plt.title("Graph of 20 highest ranking purchasing members in 2014")
bar = plt.bar(x = [str(num) for num in top20memberpurchase2014count.MemberNumber], height = [countpurchase for countpurchase in top20memberpurchase2014count.NumberPurchased], width = 0.5, color = "brown")
plt.bar_label(container = bar, labels = top20memberpurchase2014count.NumberPurchased, padding = 5)
plt.xlabel("Member Number")
plt.ylabel("Number of purchases made")
plt.show()
      
    # -- (c) Graph of member who purchased the most in 2015
membernumbers = []
datesregistered = []
for ke, va in zip(dataset.Member_number, dataset.Date):
    if va.year == 2015:
        membernumbers.append(ke)
        datesregistered.append(va)
        
memberpurchases2015 = pd.DataFrame({"Date": datesregistered, "MemberNumber": membernumbers})
memberpurchase2015count = memberpurchases2015.MemberNumber.value_counts().reset_index()
memberpurchase2015count.rename(columns = {"index": "MemberNumber", "MemberNumber": "NumberPurchased"}, inplace = True)
top20memberpurchase2015count = memberpurchase2015count.iloc[:20, :]

plt.figure(figsize = (40, 10))
plt.title("Graph of 20 highest ranking purchasing members in 2015")
bar = plt.bar(x = [str(num) for num in top20memberpurchase2015count.MemberNumber], height = [countpurchase for countpurchase in top20memberpurchase2015count.NumberPurchased], width = 0.5, color = "brown")
plt.bar_label(container = bar, labels = top20memberpurchase2015count.NumberPurchased, padding = 5)
plt.xlabel("Member Number")
plt.ylabel("Number of purchases made")
plt.show() 









# ------> SAVE ALL DATAFRAMES
transactionyearlydata.to_csv(r"VizData\transactionyearlydata.csv", index = False)
top20itemspurchased.to_csv(r"VizData\top20itemspurchased.csv", index = False)
top20leastpurchased.to_csv(r"VizData\top20leastpurchased.csv", index = False)
monthlysalesdata2014.to_csv(r"VizData\monthlysalesdata2014.csv", index = False)
monthlysalesdata2015.to_csv(r"VizData\monthlysalesdata2015.csv", index = False)
monthlysalesdata2014to2015.to_csv(r"VizData\monthlysalesdata2014to2015.csv", index = False)
datacountforitem.to_csv(r"VizData\numberofitemspurchased2014to2015.csv", index = True)
dailyitemsales2014.to_csv(r"VizData\dailyitemsales2014.csv", index = True)
dailyitemsales2015.to_csv(r"VizData\dailyitemsales2015.csv", index = True)
dailyitemsales2014to2015.to_csv(r"VizData\dailyitemsales2014to2015.csv", index = True)
data_count_member_purchase.to_csv(r"VizData\totalmemberpurchases2014to2015.csv", index = True)
memberpurchase2014count.to_csv(r"VizData\totalmemberpurchases2014.csv", index = True)
memberpurchase2015count.to_csv(r"VizData\totalmemberpurchases2015.csv", index = True)














