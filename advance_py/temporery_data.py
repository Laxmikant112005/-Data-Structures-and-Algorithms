# pip install pandas openpyxl faker

# Importing libraries

import pandas as pd
import numpy as np
from faker import Faker
import random

# Step 1: Generate Main Dataset

fake = Faker()
rows = []

for i in range(100):
    data = {
        "User_ID": fake.bothify(text="ID-CS###"),   # Random ID
        "Name": fake.name(),                        # Random Name
        "Email": fake.email(),                      # Random Email
        "Age": random.randint(20, 30),              # Age between 20–30
        "Marks": random.randint(0, 100),            # Marks between 0–100
        "Gender": random.choice(["Male", "Female"]),
        "Sub_no": random.randint(10, 24)            # Number of subjects
    }
    rows.append(data)

df = pd.DataFrame(rows)
print("Main Dataset:\n", df.head())

# Step 2: Create Pass/Fail Column

df["Passed"] = df["Marks"].apply(lambda x: "Pass" if x >= 35 else "Fail")
print("\nWith Pass/Fail:\n", df.head())

# Step 3: Generate Fee Dataset

rows = []
min_sub = df["Sub_no"].min()   # Minimum subjects

for i in df["Sub_no"]:
    back_sub = i - min_sub          # Backlog subjects
    pay = back_sub * 250            # Fee per backlog
    total = pay + 100000            # Total fee

    data = {
        "Back_sub": back_sub,
        "Pay": pay,
        "Clg_fee": 100000,          # Constant fee
        "Total": total
    }
    rows.append(data)

df1 = pd.DataFrame(rows)
print("\nFee Dataset:\n", df1.head())


# Step 4: Merge both datasets

df2 = pd.concat([df, df1], axis=1)
print("\nMerged Dataset:\n", df2.head())


# Step 5: Add Grade Column

def assign_grade(mark):
    if mark >= 95:
        return "A+"
    elif mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 55:
        return "C"
    elif mark >= 35:
        return "D"
    else:
        return "F"

df2["Grade"] = df2["Marks"].apply(assign_grade)
print("\nWith Grades:\n", df2.head())


# Step 6: Handle Missing Values

print("\nNull Values:\n", df2.isnull().sum())

# Fill numeric columns with mean (if any nulls exist)
num_cols = df2.select_dtypes(include=[np.number]).columns
df2[num_cols] = df2[num_cols].fillna(df2[num_cols].mean())



# Step 7: Encode Categorical Data


# Gender encoding
df2["Gender"] = df2["Gender"].map({
    "Male": 1,
    "Female": 0
})

# Pass/Fail encoding
df2["Passed"] = df2["Passed"].map({
    "Pass": 1,
    "Fail": 0
})



# Step 8: Drop useless columns

# Clg_fee → constant
# Total → redundant (Pay + constant)

df2.drop(columns=["Clg_fee", "Total"], inplace=True)



# Step 9: Normalize numeric data

col = ["Age", "Marks", "Sub_no", "Back_sub", "Pay"]

df2[col] = (df2[col] - df2[col].min()) / (df2[col].max() - df2[col].min())
print("\nNormalized Data:\n", df2[col].head())



# Step 10: Encode Grade (Ordinal)

df2["Grade"] = df2["Grade"].map({
    "A+": 5,
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "F": 0
})

print("\nFinal Dataset:\n", df2.head())
