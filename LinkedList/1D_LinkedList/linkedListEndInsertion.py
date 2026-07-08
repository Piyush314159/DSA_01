class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertAtEnd(self, head, x): 
        new_Node = Node(x)              # creating a new node which we want to insert at the end of the linked list

        if head is None:                # empty linked list edge case, so the new node will be the head of the linked list
            return new_Node
        
        curr = head                     # start walking from the beginning of the linked list
        while curr.next is not None:    # if the next node exist keep moving until last node
            curr = curr.next            # take one step froward
        
        curr.next = new_Node            # attach new node at the end of the linked list
        return head                     # head of the linked list remains unchanged, so return it

# creating a linked list for testing
# ===================================   
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# object of the Solution class
#==============================
sol = Solution()
head = sol.insertAtEnd(head, 6)

# Print the result
#=================
curr = head
while curr:
    if curr.next:
        print(curr.data, end=" -> ")
    else:
        print(curr.data, end=" -> None")
    curr = curr.next