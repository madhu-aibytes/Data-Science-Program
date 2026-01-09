class Queue:
    def __init__(self):
        self.items = []     # queue created

    def create_queue(self):
        return self.items   # returns queue list
# stack with queue push function OUTSIDE the class
def stack_with_queue(queue, item):
    queue.append(item)
    print("Stack with queue pushed:", item)
# create object
q = Queue() 
queue = q.create_queue()
print("Queue created for stack operations:", queue)
# stack operations using queue
n = int(input("Enter number of elements to push onto stack using queue: "))
for i in range(n):
    ele = int(input("Enter element: "))
    stack_with_queue(queue, ele)
print("Final queue representing stack:", queue)


def stack_with_queue_pop(queue):
    if len(queue) == 0:
        print("Stack with queue is empty, cannot pop.")
        return None
    item = queue.pop()  # popping from the end to simulate stack pop
    print("Stack with queue popped:", item)
    return item
# stack pop operation using queue
n = int(input("Enter number of elements to pop from stack using queue: "))
for i in range(n):
    stack_with_queue_pop(queue)
print("Final queue after stack pop operations:", queue)

