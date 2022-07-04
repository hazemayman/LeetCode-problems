# Definition for singly-linked list.
import sys
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not(list1 or list2)): return None
        if(not list1): return list2
        if(not list2): return list1
        if list1.val < list2.val:
            newList = ListNode(list1.val)
            list1 = list1.next
        else:
            newList = ListNode(list2.val)
            list2 = list2.next
        head = newList
  
        while(list1!= None or list2 !=None):
            # print(list1 , "--" , list2)
            if list1 :
                value1 = list1.val
            else:
                newList.next = ListNode(list2.val)
                list2 = list2.next
                newList = newList.next
                continue
                
            if list2 :
                value2 = list2.val
            else:
                newList.next = ListNode(list1.val)
                list1 = list1.next
                newList = newList.next
                continue

            if(value1 < value2):
                list1 = list1.next
                newList.next = ListNode(value1)
                newList = newList.next
            else:
                list2 = list2.next
                newList.next = ListNode(value2)
                newList = newList.next
                
        return head
            