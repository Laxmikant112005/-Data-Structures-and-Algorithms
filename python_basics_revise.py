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

