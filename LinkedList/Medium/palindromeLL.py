class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution1:
    def palindrome(self, head):
        curr = head
        stack = []
        while curr:
            stack.append(curr.data)
            curr = curr.next

        lo, hi = 0, len(stack) - 1
        while lo < hi:
            if stack[lo] != stack[hi]:
                return False
            lo += 1
            hi -= 1
        return True
    
# creating a linked list for testing
# ===================================
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

sol = Solution1()
print(sol.palindrome(head))


class Solution2:
    def palindrome1(self, head):
        if not head or not head.next:
            return True
        
        # finding the middle pf the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # creating the second half as a separate LL
        prev , curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # previous is now the head of the reversed second half

        left, right = head, prev
        result = True
        while right:
            if left.data != right.data:
                result = False
                break
            left = left.next
            right = right.next
        return result
    
sol1 = Solution2()
print(sol1.palindrome1(head))