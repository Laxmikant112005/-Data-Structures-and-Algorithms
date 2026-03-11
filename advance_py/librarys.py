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
print(f"Random data : \n {rand_data}")
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
