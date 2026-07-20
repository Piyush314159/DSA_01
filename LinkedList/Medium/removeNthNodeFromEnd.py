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
                nxt = curr.next.next
                curr.next = None
                curr.next = nxt
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
head.next = Node(4)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(8)

sol = Solution()
print_linked_list(head)

head1 = sol.removeNthFromEnd(head, 3)
print('\n')
print_linked_list(head1)