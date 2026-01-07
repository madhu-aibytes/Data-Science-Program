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


# insert after a given key
def insert_after_key(head, key, data):
    temp = head
    while temp:
        if temp.data == key:        # key found
            new_node = Node(data)   # create new node
            new_node.next = temp.next
            temp.next = new_node
            return head             # return updated list
        temp = temp.next
    return head                      # key not found


# insert before a given key
def insert_before_key(head, key, data):
    if head is None:
        return head

    # if key is at head
    if head.data == key:
        new_node = Node(data)
        new_node.next = head
        return new_node

    temp = head
    while temp.next:
        if temp.next.data == key:    # key found ahead
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            return head
        temp = temp.next

    return head                      # key not found


# -------------------------
# MAIN PROGRAM
# -------------------------

# create list
arr = list(map(int, input("Enter elements: ").split()))
head = create_linked_list(arr)

print("\nOriginal list:")
print_and_len(head)

# insert after key
key = int(input("\nEnter key to insert after: "))
data = int(input("Enter value to insert: "))
head = insert_after_key(head, key, data)
print("\nAfter inserting after key:")
print_and_len(head)

# insert before key
key = int(input("\nEnter key to insert before: "))
data = int(input("Enter value to insert: "))
head = insert_before_key(head, key, data)
print("\nAfter inserting before key:")
print_and_len(head)
