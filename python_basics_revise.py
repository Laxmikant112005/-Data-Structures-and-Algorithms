# Create the Dog class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says woof!")
d1 = Dog("Buddy", 3)
d1.bark()

# dictionary basic

data = {
    "name": ["laxmi", "mallikarjun", "manju"],
    "age": [10, 20, 30],
    "sall": [1000000, 200000, 300000]
}

n = len(data["name"])

for i in range(n):
    print(data["name"][i])

# average marks calculation using dictionarys

n = int(input())
student_marks = {}

for _ in range(n):
    name, *scores = input().split()
    student_marks[name] = list(map(float, scores))

query_name = input()

marks = student_marks[query_name]
average = sum(marks) / len(marks)

print(f"{average:.2f}")


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

# Fix apple and orange position calculation


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    m = len(apples)
    n = len(oranges)
    count_a = count_o = 0
    for i in range(m):
        apples[i] = apples[i] + (b)
        if apples[i] >= s and apples[i] <= t:
            count_a = count_a + 1
    
    for i in range(n):
        oranges[i] = oranges[i] + (a)
        if oranges[i] >= s and oranges[i] <= t:
            count_o = count_o + 1
    print(count_o)
    print(count_a)

app = [5, -6]
org = [-2, 2, 1]
a = 15
b = 5
s = 7
t = 11
countApplesAndOranges(s, t, a, b, app, org)


# Implement grading students rounding logic 

def gradingStudents(grades):
    n = len(grades)
    for i in range(n):
        if grades[i] >= 38:
            r = grades[i] % 5
            if r >= 3:
                grades[i] = grades[i] - r + 5
            else:
                pass
        else:
            pass
            
    return grades
    


#......................
# patterns problem 
#......................

n = 5

for i in range(1, n + 1):
    
    # increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()

# 2. .................................

n = 4

for i in range(1, n + 1):
    for j in range(n - i):
        print("  ", end="")
    for k in range(i):
        print("* ", end="")

    print()

# OUT PUT :

#       * 
#     * * 
#   * * * 
# * * * * 


# 3.  ......................................

n = 4
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# OUT PUT 

# * 
# * * 
# * * * 
# * * * * 

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

l3 = []
res = 0

for i in range(len(l1)):
    res = res + l1[i] + l2[i]
    print(res)
    r1 = res % 10
    print(r1)
    l3.append(r1)
    res = res // 10
    print(res)
    print("----------------------------")
print(l3)

# 2nd method

class Node:
    def add(self, l1, l2):
        l3 = []
        res = 0

        for i in range(len(l1)):
            res = res + l1[i] + l2[i]
            r1 = res % 10
            l3.append(r1)
            res = res // 10
        return l3
    
n = Node()
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
print(n.add(l1, l2))





        
