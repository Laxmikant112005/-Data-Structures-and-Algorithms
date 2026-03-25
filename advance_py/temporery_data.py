pip install pandas openpyxl

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
df2 = pd.concat([df, df1], axis = 1)
print(df2)

# add the Grade colomn according to the marks :
row = []
for i in df2["Marks"]:
    if i >= 95:
        res = "A+"
    elif i >= 90 and i<95:
        res = ("A")
    elif i >=75 and i < 90:
        res = ("B")
    elif i >= 55 and i < 75:
        res = ("C")
    elif i>=35 and i<55:
        res = ("D")
    else:
        res = ("F")
    data = {
        "Grade": res
    }
    row.append(data)

df3 = pd.DataFrame(row)

df4 = pd.concat([df2, df3], axis = 1)

# Converting dataFrame into Excel 
df4.to_excel("Student_data_set.xlsx", index = False)


# Handling Categorical data [(male, female), (Pass, Fail)]:

df4["Gender"] = df4["Gender"].replace({
    "Mail": "Male",
    "Femail": "Female"
})

df4["Gender"] = df4["Gender"].map({
    "Male":1,
    "Female":0
})

df4["Passed"] = df4["Passed"].map({
    "Pass":1,
    "Fail":0
})

# Categoricali handeled dataset:
print(df4["Gender"].head())
print(df4["Passed"].head())
