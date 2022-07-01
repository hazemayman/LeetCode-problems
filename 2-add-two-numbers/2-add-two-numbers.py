# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode((l1.val + l2.val) % 10)
        carry = 0
        if (l1.val + l2.val) > 9: carry = 1;
        x = newNode
        l1 = l1.next
        l2 = l2.next
        while l1 != None and l2 != None:
            newNode.next = ListNode()
            newNode =  newNode.next
            newNode.val = (carry + l1.val + l2.val) % 10
            if carry + l1.val + l2.val > 9:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            
        while(l2 != None):
            newNode.next = ListNode()
            newNode =  newNode.next
            newNode.val = (carry + l2.val) % 10
            if carry + l2.val > 9:
                carry = 1
            else:
                carry = 0

            l2 = l2.next
        while(l1 != None):
            newNode.next = ListNode()
            newNode =  newNode.next
            newNode.val = (carry + l1.val) % 10
            if carry + l1.val > 9:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
        if carry:
            newNode.next = ListNode()
            newNode =  newNode.next
            newNode.val = 1
        return x
            