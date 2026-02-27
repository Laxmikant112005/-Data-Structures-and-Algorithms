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
    
