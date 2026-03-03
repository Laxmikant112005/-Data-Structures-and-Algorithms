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
