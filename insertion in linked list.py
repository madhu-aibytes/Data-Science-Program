# Node structure
class Node:
    def __init__(self, data):
        self.data = data      # store data
        self.next = None      # pointer to next node

# create linked list from array
def create_linked_list(arr):
    head = Node(arr[0])       # first node
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])  # create next node
        temp = temp.next          # move pointer
    return head

# print list and length
def print_and_len(head):
    temp = head
    count = 0
    while temp:
        print(temp.data, end=" -> ")  # print node value
        count += 1
        temp = temp.next
    print("None")
    print("Length:", count)

# insert at beginning
def add_at_beginning(head, data):
    new_node = Node(data)     # new node
    new_node.next = head      # link new node to old head
    return new_node           # new node becomes head

# insert at end
def add_at_end(head, data):
    new_node = Node(data)
    if head is None:          # if list empty
        return new_node
    temp = head
    while temp.next:          # go to last node
        temp = temp.next
    temp.next = new_node      # attach new node at end
    return head

# insert at given position
def add_at_position(head, data, pos):
    new_node = Node(data)
    if pos == 0:              # insert at start
        new_node.next = head
        return new_node

    temp = head
    for _ in range(pos - 1):  # move to position
        if temp is None:
            return head       # invalid position
        temp = temp.next

    if temp:
        new_node.next = temp.next
        temp.next = new_node
    return head


# -------------------------
# MAIN PROGRAM
# -------------------------

# create list first
arr = list(map(int, input("Enter elements: ").split()))
head = create_linked_list(arr)

print_and_len(head)  # print original list


head = add_at_beginning(head, int(input("Enter value to add at beginning: ")))
print_and_len(head)                                          # insert at beginning


head = add_at_end(head, int(input("Enter value to add at end: ")))
print_and_len(head)                                             # insert at end               

                                                                     
data = int(input("Enter value to add at position: "))
position = int(input("Enter position: "))
head = add_at_position(head, data, position)
print_and_len(head)                                            # insert at position
                  
