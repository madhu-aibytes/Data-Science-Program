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



def heappriority_enqueue(queue, item):
    import heapq
    heapq.heappush(queue, item)
    print("Heap priority enqueued:", item)
# heappriority enqueue operation
n = int(input("Enter number of elements to heap priority enqueue: "))
for i in range(n):
    ele = int(input("Enter element: "))
    heappriority_enqueue(queue_created, ele)
print("Final heap priority queue:", queue_created)



def heappriority_dequeue(queue):
    import heapq
    if len(queue) == 0:
        print("Heap priority queue is empty, cannot dequeue.")
        return None
    item = heapq.heappop(queue)
    print("Heap priority dequeued:", item)
    return item
# heappriority dequeue operation
n = int(input("Enter number of elements to heap priority dequeue: "))
for i in range(n):
    heappriority_dequeue(queue_created)
print("Final heap priority queue after dequeue operations:", queue_created)

