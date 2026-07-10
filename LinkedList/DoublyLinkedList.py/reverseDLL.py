class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def reverseDll(self, head):
        if head is None:
            return None
        curr = head
        new_head = None
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            new_head = curr
            curr = curr.prev
        return new_head
    
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next

a = Solution()
head = a.reverseDll(head)

print("Doubly Linked List after reversal:")
curr = head
while curr:
    if curr.next:
        print(curr.data, end=" <-> ")
    else:
        print(curr.data, end=" <-> None")
    curr = curr.next