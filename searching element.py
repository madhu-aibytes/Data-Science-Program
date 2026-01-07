# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create linked list from array
def create_linked_list(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head


# print list and length
def print_and_len(head):
    temp = head
    count = 0
    while temp:
        print(temp.data, end=" -> ")
        count += 1
        temp = temp.next
    print("None")
    print("Length:", count)


# search element in linked list
def search_element(head, key):
    temp = head
    pos = 0                     # position starts from 0
    while temp:
        if temp.data == key:    # element found
            return pos
        temp = temp.next        # move to next node
        pos += 1                # increase position
    return -1                   # not found


# -------------------------
# MAIN PROGRAM
# -------------------------

# create linked list
arr = list(map(int, input("Enter elements: ").split()))
head = create_linked_list(arr)

print("\nLinked list:")
print_and_len(head)

# search element
key = int(input("\nEnter element to search: "))
position = search_element(head, key)

if position != -1:
    print(f"Element {key} found at position {position}.")
else:
    print(f"Element {key} not found in the list.")
