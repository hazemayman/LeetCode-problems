# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        startingHead = head
        before_x_greater = ListNode()
        p1 = before_x_greater
        before_x_smaller = ListNode()
        p2 = before_x_smaller
        fromX = ListNode()
        p3 = fromX
        
        condition = False
        while(head != None):
            if(head.val < x):
                a = ListNode(head.val)
                p2.next = a
                p2 = p2.next
            elif(head.val > x and not condition):
                a = ListNode(head.val)
                p1.next = a
                p1 = p1.next
            elif(head.val >= x and condition):
                a = ListNode(head.val)
                p3.next = a
                p3 = p3.next
            elif(condition == False and head.val == x):
                condition = True
                a = ListNode(head.val)
                p3.next = a
                p3 = p3.next
            head = head.next
            
        before_x_greater = before_x_greater.next
        before_x_smaller = before_x_smaller.next
        if(before_x_smaller == None) : return startingHead
        fromX = fromX.next
        if(before_x_greater != None):
            p2.next = before_x_greater
            p1.next = fromX
        else:
             p2.next = fromX
        
        
        return before_x_smaller
        
        

            
                