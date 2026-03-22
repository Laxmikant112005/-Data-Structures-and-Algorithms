# pandas library:

import pandas as pd

data = [10, 20, 30, 40, 50, 60 ]
ind = ["a", "b", "c", "d", "e", "f"]
s = pd.Series(data, index = ind)
print(f"{s}")

print(" The elements grater than 30 : \n")
print(s[s>30])
print("After adding 10 to the values :\n")
s1 = s+10
print(s1)

sum = s1.sum()
max = s1.max()
min = s1.min()
mean = s1.mean()

print(f"sum = {sum}\t max = {max}\t min = {min}\t mean = {mean} \n")

#output:
# a    10
# b    20
# c    30
# d    40
# e    50
# f    60
# dtype: int64

#  The elements grater than 30 :
# d    40
# e    50
# f    60

# After adding 10 to the values :
# a    20
# b    30
# c    40
# d    50
# e    60
# f    70

# sum = 270	 max = 70	 min = 20	 mean = 45.0



# Normalisation of data using pandas library:

import pandas as pd
import numpy as np
# random data creation 
data = np.random.randint(0, 50,10)
print(f"Random data : \n {data}")
ind = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# creating seres 
s = pd.Series(data, index = ind)
# Normalising the data
s1 = (s - s.min()) / (s.max() - s.min())
print(f"Normalized data : \n{s1.astype(int)}")


# output:

#Random data : 
 
# [11 48 16 18 15 38 47 13 26 36]

# Normalized data : 
# a    0
# b    0
# c    0
# d    0
# e    0
# f    1
# g    0
# h    0
# i    0
# j    0
# dtype: int32

# Create pandas DataFrame and demonstrate row selection using loc

import pandas as pd

data = {
    "Name" : ["laxmi", "kanta", "basu", "manju"],
    "Marks" : [50, 40, 60, 90],
    "Section" : ["A", "B", "A", "C"]
}

df = pd.DataFrame(data, index = ["student 1","student 2","student 3","student 4"] )

print(df)
print("\n ------------------------\n ")
print(df.loc["student 1"])
print("\n ------------------------\n ")
print(df.loc[["student 1", "student 3"]])

# Implement DataFrame filtering with boolean indexing and column selection

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [20, 50, 70]
}

df = pd.DataFrame(data)

print(df)

new_df = df[df["Marks"] > 40]
print(new_df)

new1_df = new_df[new_df["Marks"] > 50]
print(new1_df["Name"])

# Refactor DataFrame manipulation to use in-place column update and clearer output formatting

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 50, 70]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df["Marks"] += 5

# Handle missing values in DataFrame using mean imputation and improve code clarity

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, None, 70]
}

df = pd.DataFrame(data)

avg_marks = df["Marks"].mean()

df["Marks"] = df["Marks"].fillna(avg_marks)

print("Updated DataFrame (Missing values filled with average):")
print(df)

print("\nUpdated DataFrame (Marks increased by 5):")
print(df)

# Refactor DataFrame sorting with index normalization and improved output clarity

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 50, 70]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by="Marks", ascending=False).reset_index(drop=True)

print("Sorted DataFrame (by Marks - descending):")
print(sorted_df)


# Handled missing values and performed data filtering in Pandas DataFrame


import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Sara", "John", "Priya", "Raj", "Anu"],
    "Age": [23, np.nan, 22, 24, np.nan, 21],
    "Marks": [85, 90, np.nan, 88, 76, np.nan],
    "City": ["Delhi", "Mumbai", "Delhi", None, "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print(df)
print("\n ------Iden of Null values-------\n")
null = df.isnull()
print(null)
new_df = df[df["Age"] >20]
print("\n -------Filtering the data-------\n")
print(new_df)
print("\n -------Null in Age-------\n")
null = df[df["Age"].isnull()].index
print(df.loc[null])
print(null)
print("\n -------Age/Marks updating-------\n")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
df["City"] = df["City"].fillna("Unknown")
print(df)
print("\n -------accesing the perticular data -------\n")
temp = df.loc[0]
print(temp)
# out put :
#     Name   Age  Marks    City
# 0   Amit  23.0   85.0   Delhi
# 1   Sara   NaN   90.0  Mumbai
# 2   John  22.0    NaN   Delhi
# 3  Priya  24.0   88.0    None
# 4    Raj   NaN   76.0  Mumbai
# 5    Anu  21.0    NaN   Delhi

#  ------Iden of Null values-------

#     Name    Age  Marks   City
# 0  False  False  False  False
# 1  False   True  False  False
# 2  False  False   True  False
# 3  False  False  False   True
# 4  False   True  False  False
# 5  False  False   True  False

#  -------Filtering the data-------

#     Name   Age  Marks   City
# 0   Amit  23.0   85.0  Delhi
# 2   John  22.0    NaN  Delhi
# 3  Priya  24.0   88.0   None
# 5    Anu  21.0    NaN  Delhi

#  -------Null in Age-------

#    Name  Age  Marks    City
# 1  Sara  NaN   90.0  Mumbai
# 4   Raj  NaN   76.0  Mumbai
# Index([1, 4], dtype='int64')

#  -------Age/Marks updating-------

#     Name   Age  Marks     City
# 0   Amit  23.0   85.0    Delhi
# 1   Sara  22.5   90.0   Mumbai
# 2   John  22.0   86.5    Delhi
# 3  Priya  24.0   88.0  Unknown
# 4    Raj  22.5   76.0   Mumbai
# 5    Anu  21.0   86.5    Delhi

#  -------accesing the perticular data -------

# Name      Amit
# Age       23.0
# Marks     85.0
# City     Delhi
# Name: 0, dtype: object
