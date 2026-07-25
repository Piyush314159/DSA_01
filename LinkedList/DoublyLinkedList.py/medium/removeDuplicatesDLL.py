class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

class Solution:
    def deleteDuplicates(self, head):
        seen = set()
        curr = head
        while curr:
            if curr.data in seen:
                if curr.next:
                    curr.next.prev = curr.prev
                curr.prev.next = curr.next
                    
            else:
                seen.add(curr.data)
            curr = curr.next
        return head

def printList(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" <-> ")
        else:
            print(curr.data, end=" -> None")
        curr = curr.next
    print()

#create a doubly linked list for testing
head = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(4)
node6 = Node(4)
node7 = Node(4)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4
node5.next = node6
node6.prev = node5
node6.next = node7
node7.prev = node6

print("Original list:")
printList(head)
sol = Solution()
head = sol.deleteDuplicates(head)
print("List after removing duplicates:")
printList(head)