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



# doublely linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doublely_list:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        New_node = Node(data)
        New_node.next = self.head

        if self.head is not None:
            self.head.prev = New_node

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
        New_node.prev = temp
    
    def insert_after(self, key, data):
        New_node = Node(data)
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("The key element was not found")
            return

        New_node.next = temp.next
        New_node.prev = temp
        temp.next = New_node

        if New_node.next:
            New_node.next.prev = New_node

    def isert_position(self, pos, data):
        New_node = Node(data)

        if pos == 0:
            self.insert_front(data)
            return

        temp = self.head
        count = 0

        while temp and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of bounds")
            return

        New_node.next = temp
        New_node.prev = temp.prev

        if temp.prev:
            temp.prev.next = New_node
        temp.prev = New_node
    
    def delete(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("The key element was not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev
        
    def display(self):
        temp = self.head

        if temp is None:
            print("The list is Empty")
            return

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("NULL")
    
    def display_reverse(self):
        temp = self.head

        if temp is None:
            print("The list is Empty")
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("NULL")
obj = doublely_list()
while True:
    print("\n1. Insert Front")
    print("2. Insert Rear")
    print("3. Insert After")
    print("4. Insert Position")
    print("5. Delete")
    print("6. Display")
    print("7. Display Reverse")
    print("8. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            val = int(input("Enter value to insert: "))
            obj.insert_front(val)

        case 2:
            val = int(input("Enter value to insert: "))
            obj.insert_rear(val)

        case 3:
            key = int(input("Enter key element: "))
            val = int(input("Enter value to insert: "))
            obj.insert_after(key, val)

        case 4:
            pos = int(input("Enter position: "))
            val = int(input("Enter value to insert: "))
            obj.isert_position(pos, val)

        case 5:
            val = int(input("Enter value to delete: "))
            obj.delete(val)

        case 6:
            obj.display()

        case 7:
            obj.display_reverse()

        case 8:
            break


# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  1
# Enter value to insert:  40

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  1
# Enter value to insert:  50

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  6
# 50 <-> 40 <-> NULL

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  2
# Enter value to insert:  20

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  6
# 50 <-> 40 <-> 20 <-> NULL

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  3
# Enter key element:  20
# Enter value to insert:  30

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  6
# 50 <-> 40 <-> 20 <-> 30 <-> NULL

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  4
# Enter position:  2
# Enter value to insert:  25

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  6
# 50 <-> 40 <-> 25 <-> 20 <-> 30 <-> NULL

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  5
# Enter value to delete:  6
# The key element was not found

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  5
# Enter value to delete:  25

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  6
# 50 <-> 40 <-> 20 <-> 30 <-> NULL

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  7
# 30 <-> 20 <-> 40 <-> 50 <-> NULL

# 1. Insert Front
# 2. Insert Rear
# 3. Insert After
# 4. Insert Position
# 5. Delete
# 6. Display
# 7. Display Reverse
# 8. Exit
# Enter your choice:  8

