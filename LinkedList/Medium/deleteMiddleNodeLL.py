class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteMiddle(self, head):
        
        if not head or not head.next:
            return None
        
        dummy = Node(0)
        dummy.next = head
        slow, fast = dummy, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next

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
head.next = Node(4)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(8)

sol = Solution()
print_linked_list(head)

head1 = sol.deleteMiddle(head)
print('\n')
print_linked_list(head1)