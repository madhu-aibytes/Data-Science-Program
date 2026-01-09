class Queue:
    def __init__(self):
        self.items = []   # queue created

    def create_queue(self):
        return self.items

def kth_smallest_and_biggest(queue, k):
    if len(queue) < k:
        print("Queue has fewer than k elements.")
        return None, None
    sorted_queue = sorted(queue)
    kth_smallest = sorted_queue[k-1]
    kth_biggest = sorted_queue[-k]
    return kth_smallest, kth_biggest
# create object
q = Queue()
# call function
queue_created = q.create_queue()
print("Queue created successfully:", queue_created)
def enqueue(queue, item):
    queue.append(item)
    print("Enqueued:", item)
# enqueue operation
n = int(input("Enter number of elements to enqueue: ")) 
for i in range(n):
    ele = int(input("Enter element: "))
    enqueue(queue_created, ele)
    
    
    
print("Final queue:", queue_created)
k = int(input("Enter the value of k to find kth smallest and biggest elements: "))
kth_smallest, kth_biggest = kth_smallest_and_biggest(queue_created, k)
if kth_smallest is not None and kth_biggest is not None:
    print(f"The {k}th smallest element is: {kth_smallest}")
    print(f"The {k}th biggest element is: {kth_biggest}")
