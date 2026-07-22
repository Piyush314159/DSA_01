from requests import head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def insertNodeDLL(self, head, p, x):
        new_node = Node(x)

        if p == 0:
            new_node.next = head
            if head:                #guard against empty list
                head.prev = new_node
            return new_node

        curr = head
        count = 0
        while curr is not None and count < p - 1:
            curr = curr.next
            count += 1

        if curr is None:            # p was out of bounds
            print("Position out of bounds")
            return head
        
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        return head
            
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next

a = Solution()
head = a.insertNodeDLL(head, 5, 5)

print("Doubly Linked List after insertion:")
curr = head
while curr:
    if curr.next:
        print(curr.data, end=" <-> ")
    else:
        print(curr.data, end=" <-> None")
    curr = curr.next

