class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):

        # edge cases
        if head is None or head.next is None or k == 0:
            return head

        # calculate the length of the linked list
        len = 1
        fast = head
        while fast.next:
            fast = fast.next
            len += 1

        # calculate the effective rotations needed
        k = k % len
        if k == 0:
            return head

        # find the new head after k rotations
        rot = 1
        slow = fast = head
        while rot <= k - 1:
            fast = fast.next
            rot += 1

        # move both slow and fast pointers until fast reaches the end of the list
        prev = None
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next

        # connect the end of the list to the head and update the new head
        prev.next = None    #divide the list into two parts
        new_head = slow
        while slow.next:
            slow = slow.next
        slow.next = head    # connect the end of the second part to the head of the first part    
        return new_head

def printList(head):
    while head:
        if head.next:
            print(head.data, end="->")
        else:
            print(head.data, end="")
        head = head.next
    print()

# creating linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
print("Original Linked List:")
printList(head)

solution = Solution()
k = 4
rotated_head = solution.rotateRight(head, k)
print(f"Linked List after rotating {k} times:")
printList(rotated_head)