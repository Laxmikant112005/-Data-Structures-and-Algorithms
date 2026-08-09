# Queue insertion and deletion

from tracemalloc import start


class SinglyQueue:

    def __init__(self, size=10):
        self.queue = []
        self.size = size
        self.rear = -1

    def insert(self, value):

        if self.rear == self.size - 1:
            print("Queue is full")
            return

        self.rear += 1
        self.queue.append(value)
        print(f"Item {value} inserted successfully")

    def delete(self):

        if self.rear == -1:
            print("Queue is empty")
            return

        item = self.queue.pop(0)
        self.rear -= 1
        print(f"Item {item} deleted successfully")

    def display(self):

        if self.rear == -1:
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)


obj = SinglyQueue()

while True:

    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            item = int(input("Enter item to insert: "))
            obj.insert(item)

        case 2:
            obj.delete()

        case 3:
            obj.display()

        case 4:
            break

# improvement of double ended queue using circular queue

class double_ended_queue:
    def __init__(self, size=10):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1
    def insert_front(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size

        self.queue[self.front] = value
        print(f"Item {value} inserted at front successfully")
    def insert_rear(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(f"Item {value} inserted at rear successfully")
    def delete_front(self):
        if self.front == -1:
            print("Queue is empty")
            return

        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Item {item} deleted from front successfully")
    def delete_rear(self):
        if self.front == -1:
            print("Queue is empty")
            return

        item = self.queue[self.rear]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        print(f"Item {item} deleted from rear successfully")
    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
obj = double_ended_queue()
while True:
    print("\n1. Insert Front")
    print("2. Insert Rear")
    print("3. Delete Front")
    print("4. Delete Rear")
    print("5. Display")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            item = int(input("Enter item to insert at front: "))
            obj.insert_front(item)
        case 2:
            item = int(input("Enter item to insert at rear: "))
            obj.insert_rear(item)
        case 3:
            obj.delete_front()
        case 4:
            obj.delete_rear()
        case 5:
            obj.display()
        case 6:
            break

# Circular queue insertion and deletion

class CircularQueue:
    def __init__(self, size=10):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def insert(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Item {value} inserted successfully")

    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return

        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Item {item} deleted successfully")

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size

obj = CircularQueue()
while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            item = int(input("Enter item to insert: "))
            obj.insert(item)
        case 2:
            obj.delete()
        case 3:
            obj.display()
        case 4:
            break

