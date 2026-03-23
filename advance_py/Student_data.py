# pip install pandas openpyxl

# Importing libraries 
import pandas as pd
import numpy as np
from faker import Faker
import random


# The Main data generation 
fack = Faker()
row = []
for i in range(100):
    data = {
        "Name" : fack.name(),
        "Age" : random.randint(20, 30),
        "Marks" : random.randint(0, 100),
        "Gender" : random.choice(["Mail", "Femail"]),
        "Sub_no" : random.randint(10, 24)
    }
    row.append(data)
df = pd.DataFrame(row)  
print(df)


# Add a NEW colomn [Passed / Fail ]
row = []

for mark in df["Marks"]:
    if mark < 35:
        row.append("Fail")
    else:
        row.append("Pass")

df["Passed"] = row
print(df)

# 2nd data generating using main dataset 
row = []
min_sub = df["Sub_no"].min()
for i in df["Sub_no"]:
    res = i - min_sub
    pay = res * 250
    total = pay + 100000
    data = {
        "Back_sub" : res,
        "Pay" : pay,
        "Clg_fee" : 100000,
        "Total" : total
    }
    row.append(data)
df1 = pd.DataFrame(row)
print(df)


# Concating Two defferent dataFrame 
new_df = pd.concat([df, df1], axis = 1)
print(new_df)


# Converting dataFrame into Excel 
new_df.to_excel("Student_data_set.xlsx", index = False)