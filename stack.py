def insert(stack, item, lb, ub):

    if lb == ub + 1:
        print("stack is full")
    else:
        stack[lb] = item
        lb += 1
        print(f"Inserted {item} into stack")
    return stack

stack = [None] * 5  # Initialize stack with a fixed size of 5
for i in range(5):
    item = int(input("Enter an item to insert into stack: "))
    stack = insert(stack, item, i, len(stack) - 1)
    print(stack)