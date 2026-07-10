class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def deleteNodeDll(self, head, x):
        if head is None:
            return None
        curr = head
        while curr is not None:
            if curr.data == x:

                if curr.next is None and curr.prev is None:     # only Node
                    return None
                
                if curr.prev is None:                           # deleting the head
                    curr.next.prev = None
                    head = curr.next
                    return head
                
                if curr.next is None:                           # deleting the tail
                    curr.prev.next = None
                    return head
                
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
            curr = curr.next
        return head
    
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next

a = Solution()
head = a.deleteNodeDll(head, 4)

print("Doubly Linked List after insertion:")
curr = head
while curr:
    if curr.next:
        print(curr.data, end=" <-> ")
    else:
        print(curr.data, end=" <-> None")
    curr = curr.next