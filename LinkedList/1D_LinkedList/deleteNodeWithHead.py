# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head, x):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if head is None:
            return None
        
        if x == 1:
            return head.next
        
        prev = head
        curr = head.next
        i = 1 # tracks the position of the current
        while curr is not None:
            i += 1
            if i == x:
                prev.next = curr.next   # skip curr, relink prev -> curr.next
                break
            prev = curr
            curr = curr.next

        return head

# creating a linked list for testing
# ===================================   
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

a = Solution()
head = a.deleteNode(head, 3)

curr = head
while curr:
    if curr.next:
        print(curr.val, end=" -> ")
    else:
        print(curr.val, end=" -> None")
    curr = curr.next