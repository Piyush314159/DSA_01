# Linked List Implementation in Python

# Nodes as Class
#===============
class Node:
    def __init__(self, data):
        self.data = data   # The actual value
        self.next = None   # Pointer to next node (None = end of list)

# Building the Linked List
#=========================
class LinkedList:
    def __init__(self):
        self.head = None   # Points to the first node

# Creating nodes manually
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Linking them
n1.next = n2
n2.next = n3

# The list: 10 -> 20 -> 30 -> None
ll = LinkedList()
ll.head = n1

# Traversing the Linked List
#===========================
def print_list(ll):
    curr = ll.head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Print the linked list
#=======================
print_list(ll)  # Output: 10 -> 20 -> 30 -> None