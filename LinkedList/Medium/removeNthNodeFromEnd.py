class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        curr = head
        i = 0
        while curr:
            curr = curr.next
            i+=1
        
        if i == n:
            return head.next
        
        j = 1
        curr = head
        while curr:
            if i - j  == n:
                curr.next = curr.next.next
            curr = curr.next
            j += 1

        return head
    
def print_linked_list(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" -> ")
        else:
            print(curr.data, end=" -> None")
        curr = curr.next
    
# creating a linked list for testing
# ===================================
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

sol = Solution()
print_linked_list(head)

head1 = sol.removeNthFromEnd(head, 3)
print('\n')
print_linked_list(head1)

class Solution1:
    def removeNthFromEnd(self, head, n):
        dummy = Node(0)
        dummy.next = head
        fast = slow = dummy

        # Advance fast by n+1 steps
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast hits None
        while fast:
            fast = fast.next
            slow = slow.next    #slow stops n+1 steps behind fast

        slow.next = slow.next.next
        return dummy.next

sol1 = Solution1()
head2 = sol1.removeNthFromEnd(head, 3)
print('\n')
print_linked_list(head2)