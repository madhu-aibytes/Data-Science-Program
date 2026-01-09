class Stack:
    def __init__(self):
        self.items = []   # stack created
    def create_stack(self):
        return self.items   # returns stack list   
def queue_with_stack(stack, item):
    stack.append(item)
    print("Queue with stack enqueued:", item)
    return stack
# create object
s = Stack() 
stack = s.create_stack()
print("Stack created for queue operations:", stack)
# queue operations using stack
n = int(input("Enter number of elements to enqueue onto queue using stack: "))
for i in range(n):
    ele = int(input("Enter element: "))
    queue_with_stack(stack, ele)
print("Final stack representing queue:", stack)


# queue dequeue function OUTSIDE the class
def queue_with_stack_dequeue(stack):
    if len(stack) == 0:
        print("Queue with stack is empty, cannot dequeue.")
        return None
    item = stack.pop(0)  # popping from the start to simulate queue dequeue
    print("Queue with stack dequeued:", item)
    return item
# queue dequeue operation using stack
n = int(input("Enter number of elements to dequeue from queue using stack: "))
for i in range(n):
    queue_with_stack_dequeue(stack)
print("Final stack after queue dequeue operations:", stack)
