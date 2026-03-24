import pandas as pd
import numpy as np
from faker import Faker
import random

# -----------------------
# Data Generation
# -----------------------

fake = Faker()

data = [{
    "User_ID": fake.bothify(text="ID-CS###"),
    "Name": fake.name(),
    "Email": fake.email(),
    "Age": random.randint(20, 30),
    "Marks": random.randint(0, 100),
    "Gender": random.choice(["Male", "Female"]),
    "Sub_no": random.randint(10, 24)
} for _ in range(100)]

df = pd.DataFrame(data)

# -----------------------
# Feature Engineering
# -----------------------

# Pass/Fail
df["Passed"] = np.where(df["Marks"] < 35, "Fail", "Pass")

# Backlogs & Fees
min_sub = df["Sub_no"].min()
df["Back_sub"] = df["Sub_no"] - min_sub
df["Pay"] = df["Back_sub"] * 250
df["Clg_fee"] = 100000
df["Total"] = df["Pay"] + df["Clg_fee"]

# Grade
conditions = [
    df["Marks"] >= 95,
    df["Marks"] >= 90,
    df["Marks"] >= 75,
    df["Marks"] >= 55,
    df["Marks"] >= 35
]

grades = ["A+", "A", "B", "C", "D"]

df["Grade"] = np.select(conditions, grades, default="F")

# -----------------------
# Data Cleaning
# -----------------------

print("Null values:\n", df.isnull().sum())

num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# -----------------------
# Export
# -----------------------

df.to_excel("Student_data_set.xlsx", index=False)

print(df.head())
