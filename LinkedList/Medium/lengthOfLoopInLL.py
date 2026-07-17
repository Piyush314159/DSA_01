class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def lengthOfLoop(self, head):

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                count = 1
                curr = slow.next

                while curr != slow: # visiting all the nodes in the loop
                    curr = curr.next
                    count += 1
                return count

        return 0 
    
# creating a linked list for testing
# ===================================
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next

sol = Solution()
print(sol.lengthOfLoop(head))