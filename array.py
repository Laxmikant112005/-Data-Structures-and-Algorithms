# Finding the largest number in an array

num = [12,35,1,10,34,1]
n = num[0]
for i in num:
    if i >= n:
        n = i
    else:
        continue
print(n)

# Finding the smallest number in an array

nums = [1, 2, 4, 5, 6, 7, 8, 9, 10]
size = len(nums)
j,t = 1,1
for i in range(size):

    if j >= size:  
        break

    gap = nums[j] - nums[i]
    if gap != 1:
        print(f"Number {nums[i]} is present with gap {1}")
        print(f"\nMissing number is {j+t} with gap {gap}\n")
        j += 1
        t += 1
    else:
        j += 1
        print(f"Number {nums[i]} is present with gap {gap}")

# Finding the missing number in an array

nums = [1, 2, 4, 5, 6, 7, 8, 9, 10]

n = len(nums) + 1
xor_all = 0
xor_nums = 0

for i in range(1, n + 1):
    xor_all ^= i

for num in nums:
    xor_nums ^= num

print("Missing number is:", xor_all ^ xor_nums)

# removing duplicates from an array

nums = [4, 5, 2, 4, 1, 2, 5, 9]
res = []
j = 0
for i in nums:
    if i not in res:
        res.append(i)
        j += 1
print(res)

# Finding the majority element in an array

nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]

candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num
        
    if num == candidate:
        count += 1
    else:
        count -= 1

print("Majority element is:", candidate)

# Rotating an array by k positions

nums = [1, 2, 3, 4, 5]
k = 2

res = []
n = len(nums)

k = k % n   # safety step

for i in range(n - k, n):
    res.append(nums[i])

for i in range(0, n - k):
    res.append(nums[i])

print(res)

# Finding the maximum profit from stock prices

def max_profit(prices):
    min_price = float('inf') 
    max_profit = 0
    
    for price in prices:
       
        if price < min_price:
            min_price = price
        
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit

print(f"Max Profit: {max_profit([7, 1, 5, 3, 6, 4])}") 


# one more basic way to solve maximum profit from stock prices problem 

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


# Grouping anagrams together

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    
    for word in strs:
        sorted_key = "".join(sorted(word))
        groups[sorted_key].append(word)
    
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Grouped Anagrams: {group_anagrams(words)}")


# Finding the missing number in an array

def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum
print(f"Missing Number: {find_missing_number([3, 0, 1])}") 


---------------------------------------------------------------------

# sorting concepts **************** 

---------------------------------------------------------------------

# bubble sort 

arr = [ 20, 10, 5, 40, 100, 77, 50 ]
len = len(arr) 

for i in range(len):
    for j in range(len - 1 ):

        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print(arr)

# quick sort algorithm 

def partition( arr, lb, ub ):
    piot = arr[lb]
    start = lb
    end = ub
    while(end > start ):
        while( arr[start] <= piot ):
            start += 1
            
        while( arr[end] > piot ):
            end -= 1
            
        if end > start :
            temp = arr[start]
            arr[start]=arr[end]
            arr[end] = temp
    
    temp = arr[lb]
    arr[lb] = arr[end]
    arr[end] = temp
    return end 

def quick_sort( arr, lb, ub ):
    if lb < ub:
        loc = partition( arr, lb, ub )
        quick_sort( arr, lb, loc - 1)
        quick_sort( arr, loc + 1, ub )

arr = [ 20, 1, 30, 2, 5, 10, 15 ]
quick_sort(arr, 0, len(arr) - 1 )

print(" Sorted array is : ", arr )



