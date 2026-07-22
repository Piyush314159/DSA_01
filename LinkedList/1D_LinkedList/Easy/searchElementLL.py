class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchEl(slef, head, x):
        curr = head
        while curr:
            if curr.data == x:
                return True
            curr = curr.next
        return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

a = Solution()
print(a.searchEl(head, 6))