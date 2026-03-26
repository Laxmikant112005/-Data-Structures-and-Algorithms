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

# Pass/Fail (convert later to numeric)
df["Passed"] = np.where(df["Marks"] < 35, "Fail", "Pass")

# Backlogs & Fees
min_sub = df["Sub_no"].min()
df["Back_sub"] = df["Sub_no"] - min_sub
df["Pay"] = df["Back_sub"] * 250
df["Clg_fee"] = 100000
df["Total"] = df["Pay"] + df["Clg_fee"]

# Grade creation using conditions
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

# Check null values
print("Null values:\n", df.isnull().sum())

# Fill numeric nulls with mean
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Encoding (Categorical → Numeric)

# Gender Encoding
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

# Pass/Fail Encoding
df["Passed"] = df["Passed"].map({
    "Pass": 1,
    "Fail": 0
})

# Grade Encoding (Ordinal)
df["Grade"] = df["Grade"].map({
    "A+": 5,
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "F": 0
})


# Feature Selection (IMPORTANT)

# Drop useless / redundant columns
df.drop(columns=["User_ID", "Name", "Email"], inplace=True)

# Remove multicollinearity
df.drop(columns=["Sub_no", "Pay", "Total", "Clg_fee"], inplace=True)


# Normalization

col = ["Age", "Marks", "Back_sub"]

df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Final Output

print("\nFinal Dataset:\n", df.head())

# Export

df.to_excel("Student_data_set_cleaned.xlsx", index=False)
