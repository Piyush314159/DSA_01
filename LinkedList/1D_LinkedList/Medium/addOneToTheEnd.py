class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addOne(self, head):

        #function for reverse the linkedlist
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        #now adding the 1 and reassinging the whole linkedlist
        rev_head = reverse(head)
        curr = rev_head
        prev = None
        carry = 1
        while curr:
            curr.data += carry
            if curr.data < 10:
                carry = 0
                break
            else:
                curr.data = 0
                carry = 1
            prev = curr
            curr = curr.next
        
        if carry:
            prev.next = Node(1)
        return reverse(rev_head)
    
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
    
# creating a linked list for testing
head = Node(9)
head.next = Node(9)
head.next.next = Node(9)
head.next.next.next = Node(9)
head.next.next.next.next = Node(9)

print("Original linked list:")
printList(head)

sol = Solution()
head = sol.addOne(head)
print("Linked list after adding one:")
printList(head)