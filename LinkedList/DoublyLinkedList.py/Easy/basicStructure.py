class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

# creating nodes for testing
# ==========================
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# linking nodes to form a doubly linked list
# ==========================================
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

# creating a doubly linked list object and assigning the head
# ============================================================
dll = DLL()
dll.head = node1
dll.tail = node5

# printing the doubly linked list from head to tail
# ==========================================================
curr = dll.head
while curr:
    if curr.next:
        print(curr.data, end=" <-> ")
    else:
        print(curr.data, end=" <-> None")
    curr = curr.next
print("\n")  # for a new line after printing the list
# printing the doubly linked list from tail to head
# ==========================================================
curr = dll.tail  # starting from the tail
while curr:
    if curr.prev:
        print(curr.data, end=" <-> ")
    else:
        print(curr.data, end=" <-> None")
    curr = curr.prev