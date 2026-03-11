# Implementation of Singly Linked List in Python

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class singly_list:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        New_node = Node(data)
        New_node.next = self.head
        self.head = New_node
    
    def insert_rear(self, data):
        New_node = Node(data)

        if self.head is None:
            self.head = New_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = New_node

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        pri = None
        while temp and temp.data != key:
            pri = temp
            temp = temp.next

        if temp is None:
            print("The key element was not found")
            return

        pri.next = temp.next   # FIXED LINE

    def display(self):
        temp = self.head

        if temp is None:
            print("The list is Empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")


obj = singly_list()

while True:
    print("\n1. Insert Front")
    print("2. Insert Rear")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            val = int(input("Enter value to insert: "))
            obj.insert_front(val)

        case 2:
            val = int(input("Enter value to insert: "))
            obj.insert_rear(val)

        case 3:
            val = int(input("Enter value to delete: "))
            obj.delete(val)

        case 4:
            obj.display()

        case 5:
            break

# 0utput:

# 1. Insert Front
# 2. Insert Rear
# 3. Delete
# 4. Display
# 5. Exit
# Enter your choice: 1
# Enter value to insert: 10

# 1. Insert Front
# 2. Insert Rear
# 3. Delete
# 4. Display
# 5. Exit
# Enter your choice: 1
# Enter value to insert: 20

# 1. Insert Front
# 2. Insert Rear
# 3. Delete
# 4. Display
# 5. Exit
# Enter your choice: 2
# Enter value to insert: 30

# 1. Insert Front
# 2. Insert Rear
# 3. Delete
# 4. Display
# 5. Exit
# Enter your choice: 4
# 20 -> 10 -> 30 -> NULL

# 1. Insert Front
# 2. Insert Rear
# 3. Delete
# 4. Display
# 5. Exit
# Enter your choice: 3
# Enter value to delete: 10

# 1. Insert Front
# 2. Insert Rear
# 3. Delete
# 4. Display
# 5. Exit
# Enter your choice: 4
# 20 -> 30 -> NULL