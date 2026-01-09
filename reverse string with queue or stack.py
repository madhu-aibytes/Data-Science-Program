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



def reverse_string(queue, string):
    for char in string:
        queue.append(char)
    reversed_str = ''
    while queue:
        reversed_str += queue.pop()
    return reversed_str
# input string
input_string = input("Enter a string to reverse: ")
reversed_str = reverse_string(queue_created, input_string)
print("Reversed string:", reversed_str)
