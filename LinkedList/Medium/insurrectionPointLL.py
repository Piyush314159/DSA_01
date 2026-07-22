class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def intersectionPoint(self, headA, headB):
        currA = headA
        currB = headB

        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        
        return currA.data if currA else -1
    

# creating two linked lists for testing
# ===================================
headA = Node(1)
headA.next = Node(2)
headA.next.next = Node(3)
headA.next.next.next = Node(4)
headB = Node(3)
headB.next = Node(4)
headB.next.next = Node(5)
headB.next.next.next = Node(6)
# creating intersection
headA.next.next.next = headB.next.next
    
sol = Solution()
print("Intersection point of two linked lists:")
print(sol.intersectionPoint(headA, headB))