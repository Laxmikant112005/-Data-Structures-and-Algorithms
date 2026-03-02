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


# insertion and deletion 

def insert(stack, item, lb, ub):

    if lb == ub + 1:
        print("stack is full")
    else:
        stack[lb] = item
        lb += 1
        print(f"Inserted {item} into stack")
    return stack, lb

def deletion(stack, lb, ub):
    if lb == -1:
        print("the stack is empty")
    else:
        lb -= 1
        ele = stack.pop()
        print(f"ellement{ele} deleted succ")
    return stack, lb

stack = [None] * 5 
lb = 0
ub = len(stack)
while(lb != ub + 1):
    ch = int(input("enter your choice"))
    match ch:
        case 1:
            item = int(input("Enter an item to insert into stack: "))
            stack = insert(stack, item, lb, len(stack) - 1)
            print(stack)
        case 2:
            stack = deletion(stack,  lb, len(stack) - 1)
            print(stack)
