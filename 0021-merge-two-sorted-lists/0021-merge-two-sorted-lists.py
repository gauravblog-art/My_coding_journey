# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      
      lst1=[]
      
      while list1:
        lst1.append(list1.val)
        list1=list1.next
      
      lst2=[]
      
      while list2:
        lst2.append(list2.val)
        list2=list2.next
      
      lst3=lst1+lst2
      lst3.sort()
      
      new=temp=ListNode(0)
      
      while lst3:
        
        p=lst3.pop(0)
        node=ListNode(p)
        temp.next=node
        temp=temp.next
      return new.next
        