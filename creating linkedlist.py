'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
n1 = Node(10)   # creating of the nodes
n2 = Node(20)
n3 = Node(30)

n1.next = n2    #connecting the nodes to thenext node
n2.next = n3''' 



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head

def print_and_len(head):
    temp = head
    count = 0
    while temp:
        print(temp.data, end=" -> ")
        count += 1
        temp = temp.next
    print("None")
    print("Length:", count)

def middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


#Main part
arr = list(map(int, input("Enter elements: ").split()))  # take input
head = create_linked_list(arr)                            # create linked list
print_and_len(head)                                       # print list and length
mid = middle_node(head)                                   # find middle node
print("Middle Node:", mid.data)