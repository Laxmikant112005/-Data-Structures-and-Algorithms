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

# The Fibonacci sequence can also be generated using an iterative approach with constant space complexity.
 
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


# To find the maximum profit from buying and selling shares given an array of share prices, we can use the following code:


a = [ 12 , 13 , 11, 40 , 1, 2, 5, 20, 5 , 6]
n = len(a)
i = 0
j = n-1

while (j > i):
    if a[i] > a[i + 1]:
        max = a[i + 1]
        i += 1
    else:
        i += 1
    if a[j] < a[j - 1]:
        may = a[j - 1]
        j -= 1
    else:
        j -= 1

print(f"buy the shares at {max}")
print(f"sell the shares at {may}")
print(f"profit = {may - max}")


# To swap the values of two variables in an array, we can use a temporary variable to hold one of the values while we perform the swap. Here is an example code snippet that demonstrates how to swap the values at index 1 and index 3 in an array:


arr = [1, 2, 3, 4, 5]

temp = arr[1]
arr[1] = arr [3]
arr[3] = temp

print(arr)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)