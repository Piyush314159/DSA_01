'''
Tortoise-Hare Technique
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def middleOfLL(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def printList(node):
    while node:
        print(node.data, end=" -> " if node.next else "\n")
        node = node.next

# creating a linked list for testing
# ===================================   
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

sol = Solution()
middle = sol.middleOfLL(head)
printList(middle)