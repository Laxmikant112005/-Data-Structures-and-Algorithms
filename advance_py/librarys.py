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
