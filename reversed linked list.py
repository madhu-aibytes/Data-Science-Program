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


# reverse linked list
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next   # save next
        current.next = prev        # reverse link
        prev = current             # move prev
        current = next_node        # move current
    return prev                    # new head


# -------------------------
# MAIN PROGRAM
# -------------------------

# create list
arr = list(map(int, input("Enter elements: ").split()))
head = create_linked_list(arr)

print("\nOriginal list:")
print_and_len(head)

# reverse operation
head = reverse_linked_list(head)

print("\nReversed list:")
print_and_len(head)
