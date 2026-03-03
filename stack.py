# Stack Implementation using List (Array)

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


# Main Program
stack = []
top = -1
max_size = 5

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

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
            print("Exiting program...")
            break

        case _:
            print("Invalid choice!")

# output *******************************

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  1
# Enter item to insert:  20
# Inserted 20 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  30
# Invalid choice!

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  1
# Enter item to insert:  30
# Inserted 30 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  1
# Enter item to insert:  40
# Inserted 40 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  3
# Stack elements: [20, 30, 40]

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  1
# Enter item to insert:  50
# Inserted 50 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  1
# Enter item to insert:  45
# Inserted 45 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  3
# Stack elements: [20, 30, 40, 50, 45]

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  2
# Element 45 deleted successfully

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  3
# Stack elements: [20, 30, 40, 50]

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  3
# Stack elements: [20, 30, 40, 50]

# 1. Insert
# 2. Delete
# 3. Display
# 4. Exit
# Enter your choice:  4
# Exiting program...


def search(stack, item, lb):
    i = 0
    while i <= lb:
        if stack[i] == item:
            return i
        i += 1
    return -1   # Not found


stack = [20, 10, 50, 30, 20, 25, 5, 77, 69, 22, 47]
item = int(input("Enter item to search: "))
lb = len(stack) - 1 

result = search(stack, item, lb)

if result != -1:
    print(f"Element {item} found at index {result}")
else:
    print(f"Element {item} not found in stack")

# output : *************
# Enter item to search:  20
# Element 20 found at index 0


# Stack implementation in Python includes basic operations such as insertion, deletion, display, search and top element.

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

# Main Program
stack = []
top = -1
max_size = 5

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. search")
    print("5. Top element")
    print("6. exit...")

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
            top_item = stack[top] 
            print(f"Top element is: {top_item}")
            print(f"Length of the stack is: {len(stack)}")
            print(f"Length of the stack is: {lb + 1}")
            
        case 6:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice!")

# output *******************************

# 
# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  1
# Enter item to insert:  30
# Inserted 30 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  1
# Enter item to insert:  50
# Inserted 50 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  1
# Enter item to insert:  20
# Inserted 20 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  1
# Enter item to insert:  70
# Inserted 70 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  3
# Stack elements: [30, 50, 20, 70]

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  1
# Enter item to insert:  90
# Inserted 90 into stack

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  3
# Stack elements: [30, 50, 20, 70, 90]

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  5
# Top element is: 90
# Length of the stack is: 5
# Length of the stack is: 4

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  2
# Element 90 deleted successfully

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  5
# Top element is: 70
# Length of the stack is: 4
# Length of the stack is: 4

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  3
# Stack elements: [30, 50, 20, 70]

# 1. Insert
# 2. Delete
# 3. Display
# 4. search
# 5. Top element
# 6. exit...
# Enter your choice:  6
# Exiting program...


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

