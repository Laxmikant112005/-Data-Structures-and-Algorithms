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

# Parent Class

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal constructor called for {self.name}")

    def speak(self):
        print(f"{self.name} makes a sound")

# Child Class (Single Inheritance)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calling parent constructor
        self.breed = breed

    def speak(self):   # Method Overriding
        print(f"{self.name} barks")

    def display(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

# Multilevel Inheritance

class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} months old puppy")

# Hierarchical Inheritance

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} meows")

# Multiple Inheritance

class Walker:
    def walk(self):
        print("This animal can walk")


class Swimmer:
    def swim(self):
        print("This animal can swim")


class Duck(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"{self.name} is a duck")

# Creating Objects

print("\n--- Single Inheritance ---")
d = Dog("Buddy", "Labrador")
d.display()
d.speak()

print("\n--- Multilevel Inheritance ---")
p = Puppy("Rocky", "Beagle", 6)
p.display()
p.info()
p.speak()

print("\n--- Hierarchical Inheritance ---")
c = Cat("Kitty", "White")
c.speak()

print("\n--- Multiple Inheritance ---")
duck = Duck("Donald")
duck.show()
duck.walk()
duck.swim()
