#This program allows the user to move in four directions (right, up, down, left) and plots the path taken on a graph. The user can input their choice of direction, and the program will update the coordinates accordingly and display the graph after each move.

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
