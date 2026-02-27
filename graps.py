#This program allows the user to move in four directions (right, up, down, left) and plots the path taken on a graph. 
#The user can input their choice of direction, and the program will update the coordinates accordingly and display the graph after each move.

import matplotlib.pyplot as plt

def grap(x, y):
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

X = [0]
Y = [0]
a = 0
b = 0

def Inc(a, b):
    X.append(a)
    Y.append(b)

for i in range(10):
    ch = int(input("Enter your choice (1=Right, 2=Up, 3=Down, 4=Left): "))
    match ch:
        case 1:   # move right
            a = a + 1
            Inc(a, b)
            grap(X, Y)

        case 2:   # move up
            b = b + 1
            Inc(a, b)
            grap(X, Y)

        case 3:   # move down
            b = b - 1
            Inc(a, b)
            grap(X, Y)

        case 4:   # move left
            a = a - 1
            Inc(a, b)
            grap(X, Y)



# This program calculates the Body Mass Index (BMI) based on the user's height and weight, and also plots a pie chart showing the distribution of different BMI categories. 
# The user is prompted to enter their height in centimeters, weight in kilograms, and the amount of water they drank in liters. The BMI is calculated using the formula: 
# BMI = weight (kg) / (height (m))^2. The program then displays the calculated BMI and shows a pie chart with the distribution of BMI categories.

import matplotlib.pyplot as plt
import numpy as np
content=[
"Severe Thinness",
"Moderate Thinness",
"Mild Thinness",
"Normal",
"Overweight",
"Obese Class I",
"Obese Class II",
"Obese Class III"]
# print(content)
weight=[5,10,15,31,15,10,9,5]

plt.pie(weight,labels=content)
plt.show()

a=int(input("enter the hight in cm :"))
b=int(input("Enter the weight in kg: "))
water=int(input("how much water you drinked today in liter: "))
def BMICal(h,w):
    w=pow(w,2)
    bmi1=h/w
    bmi=bmi1*1000
    print(bmi)
    return bmi

def user(bmi=0):
    print("hello !")
    BMICal(a,b)
    

# This program demonstrates how to plot a simple graph using two arrays of data. 
# It uses the matplotlib library to create a line graph of the x and y values, and includes labels for the axes and a title for the graph. 
# The graph is displayed using the plt.show() function.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Graph of Two Arrays")

plt.show()

# This program creates a bar chart using the matplotlib library. 
# It defines two arrays, x and y, where x contains the categories (A, B, C, D) and y contains the corresponding values (10, 25, 15, 20). 
# The plt.bar() function is used to create the bar chart, and labels for the axes and a title are added for clarity. Finally, the graph is displayed using plt.show().

import matplotlib.pyplot as plt

x = ["A", "B", "C", "D"]
y = [10, 25, 15, 20]

plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# This program creates a scatter plot using the matplotlib library. 
# It defines two arrays, x and y, where x contains the x-coordinates (5, 7, 8, 10, 12, 15) and y contains the corresponding y-coordinates (12, 14, 18, 20, 22, 30).
# The plt.scatter() function is used to create the scatter plot, and labels for the axes and a title are added for clarity. Finally, the graph is displayed using plt.show().

import matplotlib.pyplot as plt

x = [5, 7, 8, 10, 12, 15]
y = [12, 14, 18, 20, 22, 30]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
