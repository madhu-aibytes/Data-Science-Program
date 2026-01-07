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


# delete first node
def delete_first(head):
    if head is None:          # empty list
        return None
    return head.next          # new head becomes 2nd node


# delete last node
def delete_last(head):
    if head is None:          # empty list
        return None
    if head.next is None:     # one node
        return None

    temp = head
    while temp.next.next:     # reach 2nd last node
        temp = temp.next
    temp.next = None          # remove last node
    return head


# delete node at given position
def delete_at_position(head, pos):
    if pos == 0:              # delete first
        return delete_first(head)

    temp = head
    for _ in range(pos - 1):  # move to previous node
        if temp is None or temp.next is None:
            return head       # invalid position
        temp = temp.next

    temp.next = temp.next.next
    return head


# -------------------------
# MAIN PROGRAM
# -------------------------

# create linked list
arr = list(map(int, input("Enter elements: ").split()))
head = create_linked_list(arr)

print("\nOriginal list:")
print_and_len(head)

# delete first node
head = delete_first(head)
print("\nAfter deleting first node:")
print_and_len(head)

# delete last node
head = delete_last(head)
print("\nAfter deleting last node:")
print_and_len(head)

# delete at given position
pos = int(input("\nEnter position to delete: "))
head = delete_at_position(head, pos)
print("\nAfter deleting at given position:")
print_and_len(head)
