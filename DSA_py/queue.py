# Queue insertion and deletion

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


# Double ended queue insertion and deletion

class  Doublended_queue :
    def __init__(self, queue, size = 10, start = -1, rear = -1):
        self.queue = queue
        self.size = size
        self.rear = rear
        
    def insert_front(self, value):
        if self.rear == self.size - 1:
            print(" The queue is full")
        else:
            self.rear += 1
            self.queue.insert(0, value)
        return value
        
    def insert_rear(self, value):
        if self.rear == self.size - 1:
              print("the queue is full")
        else:
            self.rear += 1
            self.queue.append(value)
        return value
        
    def delete_front(self):
        if self.rear == -1:
            print(" The que is empty:")
            return 0
        else:
            self.res = self.queue[0]
            self.queue.remove(self.queue[0])
            self.rear -= 1
            return self.res

    def delete_rear(self):
        if self.rear == -1:
            print("The queue is empty: ")
        else:
            self.res = self.queue[self.rear]
            self.queue.pop()
            self.rear -= 1
            return self.res
    def desplay(self):
        print(self.queue)

queue = []

obj = Doublended_queue(queue)

while(True):
    print("1. insert_front. \t 2. insert_rear \t 3. delete_front \t 4. delete_rear \t 5. desplay \n")
    ch = int(input(" enter your choice \n"))
    
    match ch:
        case 1:
            item = int(input("Enter item to insert : "))
            res = obj.insert_front(item)
            print(f" item {res} inserted sccu")
        case 2:
            item = int(input("Enter item to insert : "))
            res = obj.insert_rear(item)
            print(f" item {res} inserted sccu")
        case 3:
            res = obj.delete_front()
            print(f" iten {res} deleted sccu")
        case 4:
            res = obj.delete_rear()
            print(f" iten {res} deleted sccu")
        case 5:
            obj.desplay()
        case 6:
            break


# output : 


# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  1
# Enter item to insert :  50
#  item 50 inserted sccu
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  1
# Enter item to insert :  30
#  item 30 inserted sccu
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  2
# Enter item to insert :  70
#  item 70 inserted sccu
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  2
# Enter item to insert :  90
#  item 90 inserted sccu
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  5
# [30, 50, 70, 90]
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  3
#  iten 30 deleted sccu
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  5
# [50, 70, 90]
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  4
#  iten 90 deleted sccu
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  5
# [50, 70]
# 1. insert_front. 	 2. insert_rear 	 3. delete_front 	 4. delete_rear 	 5. desplay 

#  enter your choice 
#  6