class Stack:
    def __init__(self):
        self.items = []   # stack created
def input_stack():
    s = Stack()
    elements = list(map(int, input("Enter stack elements (space-separated): ").split()))
    for elem in elements:
        s.items.append(elem)   # push elements onto stack
    return s
def print_stack(s):
    print("Stack elements (top to bottom):")
    for item in reversed(s.items):
        print(item)


# Main part
stack = input_stack()    # input stack  
print_stack(stack)      # print stack



def len_stack(s):
    return len(s.items)   # return length of stack  
print("Length of stack:", len_stack(stack))  # print length of stack

