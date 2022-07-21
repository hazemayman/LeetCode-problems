# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(left == right):
            return head
        originalHead = head
        prevhead = None
        counter = 1
        while(counter != left):
            prevhead = head
            head = head.next
            counter+=1
        firstInSeq = head
        Node1 = head
        head = head.next
        counter+=1
        while(counter != right):
            nextNode = head.next
            head.next = Node1
            Node1 = head
            head = nextNode
            counter+=1

        firstInSeq.next = head.next
        head.next = Node1
        if(prevhead == None):
            originalHead = head
        else:
            prevhead.next = head
        return originalHead
        
            