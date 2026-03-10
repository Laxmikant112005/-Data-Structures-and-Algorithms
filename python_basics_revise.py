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