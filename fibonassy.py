#To generate a Fibonacci number  using a loop, we can use the following code:

arr = []
for i in range(10):
    if i<2:
        arr.append(i)
    else:
        key=arr[i-2]+arr[i-1]
        arr.append(key)
        
print(arr)

#To generate a Fibonacci number using recursion, we can use the following code:

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)  

n = 10
fib_sequence = [fib(i) for i in range(n)]
print(fib_sequence)  

#the n+1 th Fibonacci number is given by fib(n) where n is the index of the Fibonacci number we want to calculate. 
#For example, if we want to calculate the 11th Fibonacci number,
#we can call fib(10) and it will return the value of the 11th Fibonacci number.

print(fib(n))

#The Fibonacci sequence can also be generated using dynamic programming to optimize the recursive approach.

def fib_dp(n, memo={}):

    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

n = 10

fib_sequence = [fib_dp(i) for i in range(n)]
print(fib_sequence)

#The Fibonacci sequence can also be generated using an iterative approach with constant space complexity.
 
def fib_iter(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 10

fib_sequence = [fib_iter(i) for i in range(n)]
print(fib_sequence)