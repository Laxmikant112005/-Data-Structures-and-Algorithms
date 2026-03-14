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

