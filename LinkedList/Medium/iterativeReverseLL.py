class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverseLL(self, head):

        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# creating a linked list for testing
# ===================================   
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

sol = Solution()
reversed_head = sol.reverseLL(head)
curent = reversed_head
while curent:
    print(curent.data, end=" -> " if curent.next else "\n")
    curent = curent.next