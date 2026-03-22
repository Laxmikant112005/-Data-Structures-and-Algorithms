import pandas as pd
import numpy as np

data = {
    "Name":["Laxmi", "Mullu", "basu", "MUNJU", "MoNi", "Likii"],
    "Age":[20, "30", 30, 20, 25, 35]
}

df = pd.DataFrame(data, index = ["person1", "person2","person3","person4","person5","person6"])

print(df)

# inconsistent data:

df["Name"] = df["Name"].str.lower()

print(df["Name"])

# sorting df with respect to Alpabet

df= df.sort_values(by = "Name", ascending = True)

print(df)

# Incorrect datatype

df["Age"]=df["Age"].astype(int)

print(df)


# load the excel dataset

df1 = pd.read_excel("Customer-Purchase-History.xlsx")

print(df1.head(10))

print(df1.tail())

# accrtact the laptop infomation 

df1 = df1[df1["product"] == "laptop"]
