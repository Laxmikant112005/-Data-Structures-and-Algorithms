# Count the number of occurrences of an element in a stack

def count(stack, val, i, lb):
    count = 0
    while(i <= lb):
        if stack[i] == val:
            count += 1
            i += 1
        else:
            i += 1
    return count

stack = [ 20, 20, 20, 30, 20, 50, 30, 40, 30 ]
val = int(input("Enter the value "))
count = count(stack, val, 0, len(stack) - 1)
print(count)

#Enter the value  30
#3



# Stack implementation in Python includes basic operations such as insertion, deletion, display, search, top element and occurrence of an element in a stack.

def insert(stack, item, top, max_size):
    if top == max_size - 1:
        print("Stack Overflow! Stack is full.")
    else:
        top += 1
        stack.append(item)
        print(f"Inserted {item} into stack")
    return stack, top


def deletion(stack, top):
    if top == -1:
        print("Stack Underflow! Stack is empty.")
    else:
        ele = stack.pop()
        print(f"Element {ele} deleted successfully")
        top -= 1
    return stack, top


def search(stack, item, lb):
    i = 0
    while i <= lb:
        if stack[i] == item:
            return i
        i += 1
    return -1  


def count_occurrence(stack, val, i, lb):
    cnt = 0
    while i <= lb:
        if stack[i] == val:
            cnt += 1
        i += 1
    return cnt


# Main Program
stack = []
top = -1
max_size = 5

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Search")
    print("5. Top element")
    print("6. No. occurrence")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            item = int(input("Enter item to insert: "))
            stack, top = insert(stack, item, top, max_size)

        case 2:
            stack, top = deletion(stack, top)

        case 3:
            if top == -1:
                print("Stack is empty")
            else:
                print("Stack elements:", stack)

        case 4:
            item = int(input("Enter item to search: "))
            lb = len(stack) - 1
            result = search(stack, item, lb)
            if result != -1:
                print(f"Element {item} found at index {result}")
            else:
                print(f"Element {item} not found in stack")

        case 5:
            if top == -1:
                print("Stack is empty")
            else:
                top_item = stack[top]
                print(f"Top element is: {top_item}")
                print(f"Length of the stack is: {len(stack)}")

        case 6:
            if top == -1:
                print("Stack is empty")
            else:
                val = int(input("Enter the value: "))
                result = count_occurrence(stack, val, 0, len(stack) - 1)
                print(f"{val} occurs {result} times")

        case 7:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice!")

# output:...................................................................

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  1
# Enter item to insert:  20
# Inserted 20 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  3
# Stack elements: [20]

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  6
# Enter the value:  10
# 10 occurs 0 times

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  1
# Enter item to insert:  40
# Inserted 40 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  6
# Enter the value:  10
# 10 occurs 0 times

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  1
# Enter item to insert:  10
# Inserted 10 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  3
# Stack elements: [20, 40, 10]

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  5
# Top element is: 10
# Length of the stack is: 3

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  4
# Enter item to search:  10
# Element 10 found at index 2

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  6
# Enter the value:  20
# 20 occurs 1 times

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  1
# Enter item to insert:  20
# Inserted 20 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  6
# Enter the value:  20
# 20 occurs 2 times

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  3
# Stack elements: [20, 40, 10, 20]

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  1
# Enter item to insert:  50
# Inserted 50 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  5
# Top element is: 50
# Length of the stack is: 5

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  4
# Enter item to search:  50
# Element 50 found at index 4

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  2
# Element 50 deleted successfully

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  3
# Stack elements: [20, 40, 10, 20]

# 1. Insert
# 2. Delete
# 3. Display
# 4. Search
# 5. Top element
# 6. No. occurrence
# 7. Exit
# Enter your choice:  7
# Exiting program...