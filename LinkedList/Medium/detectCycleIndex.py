class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def detectCycle(self, head):

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
    
# creating a linked list for testing
# ===================================
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next

sol = Solution()
print(sol.detectCycle(head))