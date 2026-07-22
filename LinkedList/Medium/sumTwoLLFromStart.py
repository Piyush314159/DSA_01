class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoNumbers(self, headA, headB):
        currA = headA
        currB = headB
        carry = 0
        dummy = Node(0)
        curr = dummy
        while currA or currB or carry:

            a = currA.data if currA else 0
            b = currB.data if currB else 0

            total = a + b + carry
            carry = total // 10
            digit = total % 10

            curr.next = Node(digit)
            curr = curr.next

            if currA:
                currA = currA.next
            if currB:
                currB = currB.next

        return dummy.next

def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# creating two linked lists for testing
headA = Node(2)
headA.next = Node(4)
headA.next.next = Node(9)
#headA.next.next.next = Node(9)
#headA.next.next.next.next = Node(9)
#headA.next.next.next.next.next = Node(9)

headB = Node(5)
headB.next = Node(6)
headB.next.next = Node(4)
headB.next.next.next = Node(9)

print("Original linked list A:")
printList(headA)
print("Original linked list B:")
printList(headB)

sol = Solution()
headA = sol.addTwoNumbers(headA, headB)
print("Linked list after adding two numbers:")
printList(headA)
