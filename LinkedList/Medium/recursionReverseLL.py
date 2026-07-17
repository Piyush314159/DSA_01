class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverseLL(self, head):
        def rec(head):
            # base case: empty list or single node
            if head is None or head.next is None:
                return head

            # reverse everything after head; new_head is the final head of the reversed list
            new_head = rec(head.next)

            # fix the local connection: make the next node point back to head
            head.next.next = head
            head.next = None  # detach to avoid a cycle
            return new_head

        return rec(head)


# creating a linked list for testing
# ===================================
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

sol = Solution()
reversed_head = sol.reverseLL(head)

curr = reversed_head
while curr:
    print(curr.data, end=" -> " if curr.next else "\n")
    curr = curr.next