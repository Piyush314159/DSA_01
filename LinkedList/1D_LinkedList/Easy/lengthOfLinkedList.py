class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def lengthLL(self, head):
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        return length
    
# creating a linked list for testing
# ===================================   
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(5)

a = Solution()
print(a.lengthLL(head))