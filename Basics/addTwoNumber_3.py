class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# List 1: 2 → 4 → 3

#creating three different nodes (or objects) with different values

l1_1 = ListNode(2)#val=2
l1_2 = ListNode(4)#val=4
l1_3 = ListNode(3)#val=3

#creating the linked list
l1_1.next = l1_2
l1_2.next = l1_3

l1 = l1_1#just renaming the head l1_1 as l1


# List 2: 5 → 6 → 4
l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)

l2_1.next = l2_2
l2_2.next = l2_3

l2 = l2_1 #head of the list

class Solution:
    def addTwoNumbers(self, l1, l2) :
        
        a=l1
        b=l2
        carry=0
        dummy=ListNode(0) #dummy listnode 
        current=dummy
        while a or b or carry: #when one of them is True Carry=0 =>False
            val_a = a.val if a else 0 #if ListNode-a has a value on that node then it will atke the value otherwise it will take 0
            val_b = b.val if b else 0
            total=val_a+val_b+carry #adding the components of two lists
            a1=a.next if a else None #if ListNode-a has a value on that node it will take that value otherwise it will take None
            b1=b.next if b else None
            carry=total//10 #after dividing it will take the integer value
            total=total%10 #remainder
            
            current.next=ListNode(total) #assigning the list node
            current=current.next #creating the linked list

            a=a1
            b=b1
        return dummy.next #dummmy.next is the actual head