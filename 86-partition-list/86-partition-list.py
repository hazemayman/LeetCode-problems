# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_x_smaller = ListNode()
        p1 = before_x_smaller
        fromX = ListNode()
        p2 = fromX
        
        condition = False
        while(head != None):
            if(head.val < x):
                a = ListNode(head.val)
                p1.next = a
                p1 = p1.next
            elif(head.val >= x):
                a = ListNode(head.val)
                p2.next = a
                p2 = p2.next
            head = head.next
            
        before_x_smaller = before_x_smaller.next
        fromX = fromX.next
        if(before_x_smaller == None) : return fromX
        p1.next = fromX
        return before_x_smaller
        

            
                