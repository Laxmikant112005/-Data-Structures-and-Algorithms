# Data_Structures and Algorithms

Data Structures and Algorithms (DSA) is a core concept in computer science used to organize data efficiently and solve problems effectively.

Data Structures help store and manage data

Example 

    arrays, linked lists, stacks, queues, trees, graphs.

Algorithms are step-by-step procedures to solve problems

Example 
     
     sorting, searching.

Why DSA is Important?

Improves problem-solving skills

Helps write optimized and efficient code

Essential for coding interviews and competitive programming



# Fibonacci Sequence in Python 🐍

This project demonstrates different ways to generate the Fibonacci sequence in Python.

The Fibonacci sequence:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

Each number is the sum of the two previous numbers.

---

## Methods Implemented

### 1️⃣ Using Loop (List)

* Builds the sequence using a `for` loop.
* **Time:** O(n)
* **Space:** O(n)

---

### 2️⃣ Using Recursion

* Uses formula: `F(n) = F(n-1) + F(n-2)`
* **Time:** O(2ⁿ) (slow for large n)
* **Space:** O(n)

---

### 3️⃣ Using Dynamic Programming (Memoization)

* Stores previously calculated values.
* **Time:** O(n)
* **Space:** O(n)

---

### 4️⃣ Iterative (Constant Space) ✅

* Uses two variables instead of a list.
* **Time:** O(n)
* **Space:** O(1)
* **Most efficient method**


📘 Array Problem Solving in Python

This file contains basic to intermediate array (list) problems implemented in Python. The purpose of this project is to strengthen logical thinking, problem-solving skills, and understanding of Data Structures & Algorithms (DSA).

🚀 Problems Implemented
1️⃣ Finding the Largest Element

Iterates through the list

Compares each element to track the maximum value

Time Complexity: O(n)

---

### 2️⃣ Finding the Missing Number (Gap Method)

Detects missing number by checking difference between consecutive elements

Demonstrates analytical reasoning

---

### 3️⃣ Finding the Missing Number (XOR Method)

Uses bitwise XOR operation

Optimized and interview-focused approach

Time Complexity: O(n)

Space Complexity: O(1)

---

### 4️⃣ Removing Duplicates (Without Using Set)

Preserves original order

Avoids built-in set function

Time Complexity: O(n²) (due to membership checking)

---

### 5️⃣ Finding the Majority Element

Implements Boyer-Moore Voting Algorithm

Efficient interview-level solution

Time Complexity: O(n)

Space Complexity: O(1)

---

### 6️⃣ Rotating an Array by K Positions

Rotates elements to the right

Handles large values of k using modulo operation

Time Complexity: O(n)

---

