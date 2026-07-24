class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def deleteNode(self, head, k):
        curr = head
        while curr:
            if curr.data == k:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            curr = curr.next
        return head

def printList(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" <-> ")
        else:
            print(curr.data, end=" ")
        curr = curr.next
    print()

# create a doubly linked list for testing
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4


printList(head)

sol = Solution()
head = sol.deleteNode(head, 3)
printList(head)