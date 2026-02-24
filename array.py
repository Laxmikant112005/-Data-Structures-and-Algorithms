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