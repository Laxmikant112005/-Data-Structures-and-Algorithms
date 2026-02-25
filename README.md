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

# Python Analytical Problem Solving 🐍

This repository contains optimized Python solutions for classic analytical and algorithmic problems. Each solution is designed with a focus on **Time Complexity ($O$ notation)** and efficient use of Python's built-in data structures.

---

## 🚀 Problems & Solutions

### 1. Stock Whisperer (Array Analysis)
**Problem:** Find the maximum profit possible by buying a stock on one day and selling it on a future day.
* **Logic:** Instead of nested loops, we use a **Single Pass** approach. We track the `min_price` seen so far and calculate the potential profit at every step.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$

### 2. Anagram Grouper (Hash Maps)
**Problem:** Group a list of strings into sub-lists where each sub-list contains words that are anagrams of each other.
* **Logic:** Uses a `dictionary` (Hash Map) where the **sorted version** of the word acts as the key (e.g., "eat" and "tea" both become "aet").
* **Time Complexity:** $O(n \cdot k \log k)$ (where $k$ is the length of the longest word).
* **Space Complexity:** $O(n \cdot k)$



### 3. The Missing Link (Mathematical Logic)
**Problem:** Given an array containing $n$ distinct numbers in the range $[0, n]$, find the one number that is missing.
* **Logic:** Uses **Gauss's Summation Formula**. By calculating what the sum *should* be and subtracting the *actual* sum, the remainder is our missing value.
* **Formula:** $$\sum_{i=0}^{n} i = \frac{n(n+1)}{2}$$
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$

---

## 📊 Customer Behavior Analytics (OOP)
**Goal:** Transform raw transaction logs into actionable business intelligence using RFM (Recency, Frequency, Monetary) analysis.

### Key Features:
* **Data Ingestion:** Parses string-based dates and amounts into Python `datetime` objects.
* **RFM Logic:** Implements a custom scoring algorithm to rank customers based on loyalty and spending.
* **Churn Detection:** Automatically flags customers as "At Risk" if their recency exceeds 30 days.



[Image of RFM analysis model diagram]


### Technical Highlights:
* **OOP Design:** Encapsulates logic within a `RetailAnalytics` class for reusability.
* **Sorting & Lambda:** Uses complex sorting to rank data by calculated scores.
* **Time Complexity:** $O(N)$ for data ingestion and $O(M \log M)$ for reporting (where $M$ is the number of unique customers).
