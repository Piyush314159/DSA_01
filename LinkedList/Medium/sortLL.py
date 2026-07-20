class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortLL(self, head):
        curr = head
        stack = []
        while curr:
            stack.append(curr.data)
            curr = curr.next
        
        stack.sort()

        curr = head
        for val in stack:
            curr.data = val
            curr = curr.next
        return head

def print_linked_list(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" -> ")
        else:
            print(curr.data, end=" -> None")
        curr = curr.next
    
# creating a linked list for testing
# ===================================
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(5)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

print_linked_list(head)
print('\n')

sol = Solution()
head = sol.sortLL(head)
print_linked_list(head)