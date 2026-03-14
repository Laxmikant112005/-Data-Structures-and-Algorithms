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

