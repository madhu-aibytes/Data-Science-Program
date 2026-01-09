class Queue:
    def __init__(self):
        self.items = []     # queue created

    def create_queue(self):
        return self.items   # returns queue list

# create object
q = Queue()
queue = q.create_queue()
print("Queue created:", queue)

# enqueue function OUTSIDE the class
def enqueue(queue, item):
    queue.append(item)
    print("Enqueued:", item)

# enqueue operation
n = int(input("Enter number of elements to enqueue: "))
for i in range(n):
    ele = int(input("Enter element: "))
    enqueue(queue, ele)
print("Final queue:", queue)