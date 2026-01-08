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



def push_element(s, element):
    s.items.append(element)   # push element onto stack
    return s
# push element
element = int(input("Enter element to push onto stack: "))  
stack = push_element(stack, element)
print("\nStack after pushing element:")
print_stack(stack)      # print stack after pushing element
print("Length of stack after pushing element:", len_stack(stack))  # print length after pushing element
