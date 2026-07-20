
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

	
class Solution:
    def segregate(self, head):

        dummy0 = Node(-1)
        dummy1 = Node(-1)
        dummy2 = Node(-1)

        tail0 = dummy0
        tail1 = dummy1
        tail2 = dummy2

        curr = head
        while curr:
            if curr.data == 0:
                tail0.next = curr
                tail0 = tail0.next
            elif curr.data == 1:
                tail1.next = curr
                tail1 = tail1.next
            else:
                tail2.next = curr
                tail2 = tail2.next
            curr = curr.next
        
        tail2.next = None
        tail1.next = dummy2.next
        tail0.next = dummy1.next
        
        return dummy0.next

def print_linked_list(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" -> ")
        else:
            print(curr.data, end=" -> None")
        curr = curr.next
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)
head.next.next.next.next.next.next = Node(1)
head.next.next.next.next.next.next.next = Node(2)

sol = Solution()
head = sol.segregate(head)
print_linked_list(head)

 