# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val)//10
        x = newNode
        l1 = l1.next
        l2 = l2.next
        while l1 or l2 or carry :
            newNode.next = ListNode()
            newNode =  newNode.next
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            s = carry + value1 + value2
            newNode.val = s % 10
            carry = s//10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return x
            