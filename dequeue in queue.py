class Queue:
    def __init__(self):
        self.items = []   # queue created

    def create_queue(self):
        return self.items
# create object
q = Queue()
# call function
queue_created = q.create_queue()
print("Queue created successfully:", queue_created)



# enqueue function OUTSIDE the class
def enqueue(queue, item):
    queue.append(item)
    print("Enqueued:", item)

# enqueue operation
n = int(input("Enter number of elements to enqueue: "))
for i in range(n):
    ele = int(input("Enter element: "))
    enqueue(queue_created, ele)
print("Final queue:", queue_created)

def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty, cannot dequeue.")
        return None
    item = queue.pop(0)
    print("Dequeued:", item)
    return item
# dequeue operation
n = int(input("Enter number of elements to dequeue: "))
for i in range(n):
    dequeue(queue_created)
print("Final queue after dequeue operations:", queue_created)


