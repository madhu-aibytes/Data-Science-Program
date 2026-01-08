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
    print()
    for item in reversed(s.items):
        print(item)


# Main part
stack = input_stack()    # input stack  
print_stack(stack)      # print stack



def len_stack(s):
    return len(s.items)   # return length of stack  
print("Length of stack:", len_stack(stack))  # print length of stack






def overflow_stack(s, limit):
    if len(s.items) >= limit:
        print("Stack overflow. Cannot push more elements.")
        return True
    return False   # check overflow     
# check overflow
limit = int(input("Enter stack limit for overflow check: "))
if overflow_stack(stack, limit):
    exit()
print("Stack has space. No overflow.")  








def push_element(s, element):
    s.items.append(element)   # push element onto stack
    return s
# push element
element = int(input("Enter element to push onto stack: "))          
stack = push_element(stack, element)
print("\nStack after pushing element:")
print_stack(stack)      # print stack after pushing element
print("Length of stack after pushing element:", len_stack(stack))  # print length after pushing



def unflow_stack(s):
    if len(s.items) == 0:
        print("Stack is empty. Cannot perform underflow.")
        return True
    return False   # check underflow
# check underflow       
if unflow_stack(stack):
    exit()
print("Stack is not empty. No underflow.")


def pop_element(s):
    if len(s.items) == 0:
        print("Stack is empty. Cannot pop element.")
        return None
    return s.items.pop()   # pop element from stack 
# pop element
popped = pop_element(stack)
if popped is not None:
    print(f"\nPopped element: {popped}")
    print("Stack after popping element:")
    print_stack(stack)      # print stack after popping element
    print("Length of stack after popping element:", len_stack(stack))  # print length after popping element
    



def peek_stack(s):
    if len(s.items) == 0:
        print("Stack is empty. Cannot peek element.")
        return None
    return s.items[-1]   # peek element from stack      
# peek element
top_element = peek_stack(stack)
if top_element is not None:
    print(f"\nTop element (peek): {top_element}")
    print("Stack after peeking element:")
    print_stack(stack)      # print stack after peeking element
    print("Length of stack after peeking element:", len_stack(stack))  # print length






    