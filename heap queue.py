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

def heapqueue(queue, item):
    import heapq
    heapq.heappush(queue, item)
    print("Heapqueued:", item)
# heapqueue operation
n = int(input("Enter number of elements to heapqueue: "))   
for i in range(n):
    ele = int(input("Enter element: "))
    heapqueue(queue_created, ele)
print("Final heap queue:", queue_created)


def heappop(queue):
    import heapq
    if len(queue) == 0:
        print("Heap queue is empty, cannot heappop.")
        return None
    item = heapq.heappop(queue)
    print("Heappopped:", item)
    return item     
# heappop operation
n = int(input("Enter number of elements to heappop: "))
for i in range(n):
    heappop(queue_created)
print("Final heap queue after heappop operations:", queue_created)



 