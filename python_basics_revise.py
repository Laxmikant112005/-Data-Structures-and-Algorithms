# Create the Dog class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says woof!")
# Create an object
d1 = Dog("Buddy", 3)
# Call the bark method
d1.bark()

# Finding the sum of all elements in an array
# in pattern of hourglass
# 1 2 3
#   4
# 5 6 7
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12],
       [13, 14, 15]]

ar = []
n = len(arr)
m = len(arr[0])

for i in range(n - 2):
    for j in range(m - 2):
        total = (
            arr[i][j] + arr[i][j+1] + arr[i][j+2] +
            arr[i+1][j+1] +
            arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        )
        ar.append(total)

print(ar)

# Finding the sum of the primary and secondary diagonals of a square matrix

arr = [[1, 2, 4],
       [4, 5, 6],
       [7, 8, 9]]
n = len(arr)
sum1 = sum2 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum1 += arr[i][j]

for i in range(n):
        for j in range(n - 1, -1, -1):
            if n - i - 1 == j:
                sum2 += arr[i][j]
print(sum1)
print(sum2)

# Finding the ratio of positive, negative and zero elements in an array

arr = [-4, 3, -9, 0, 4, 1]
def plusMinus(arr):
    # Write your code here
    c1 = c2 = c3 = 0
    n = len(arr)
    for i in arr:
        if i > 0:
            c1 += 1
        elif i < 0:
            c2 += 1
        else:
            c3 += 1
    print(c1, c2, c3, n)
    c1 = c1 / n
    c2 = c2 / n
    c3 = c3 / n
    print(f"{c1:.6f}")
    print(f"{c1:.6f}")
    print(f"{c1:.6f}")

plusMinus(arr)


#          *
#        * *
#      * * *

# printing the above pattern
n = 3
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()

# convert array into a string and vice versa
arr = ['H', 'e', 'l', 'l', 'o', 1, 2, 3]
string = ''.join(map(str, arr))
print("String:", string)

new_arr = list(string)
print("Array:", new_arr)

# finding sub string in a string by index
s = '12:00:01AM'
s = '12:00:01PM'
print(len(s))
res = int(s[0:2])
res = res % 12
if s[-2:] == 'PM':
    res += 12
print(f"{res:02d}{s[2:8]}")

# the working of dictionares

arr = []
a = [20, 30, 10, 40]
i = 0
for i in a:
    add = i + 5
    sub = i - 10
    data = {
        "Add":add,
        "Sub":sub
    }
    arr.append(data)
print(arr)