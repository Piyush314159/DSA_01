class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

class Solution:
    def findPairsWithGivenSum(self, target, head):
        tail = head
        while tail.next:
            tail = tail.next

        left, right = head, tail
        result = []

        while left != right and left.prev != right:
            current_sum = left.data + right.data

            if current_sum == target:
                result.append([left.data, right.data])
                left = left.next
                right = right.prev

            elif current_sum < target:
                left = left.next

            else:
                right = right.prev
        return result

#create a doubly linked list for testing
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

sol = Solution()
target_sum = 5
pairs = sol.findPairsWithGivenSum(target_sum, head)
print(f"Pairs with sum {target_sum}: {pairs}")