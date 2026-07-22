class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def oddEven(self, head):
        if not head:
            return head
        
        odd_dummy = head
        even_dummy = Node(-1)
        odd_tail = odd_dummy
        even_tail = even_dummy

        curr = head.next
        i = 2
        while curr:
            if i % 2 == 1:
                odd_tail.next = curr
                odd_tail = odd_tail.next
            else:
                even_tail.next = curr
                even_tail = even_tail.next
            curr = curr.next
            i += 1

        even_tail.next = None
        odd_tail.next = even_dummy.next
        return odd_dummy
    
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

print_linked_list(head)

sol = Solution()
head1 = sol.oddEven(head)

print("\nAfter rearranging odd and even nodes:")
print_linked_list(head1)