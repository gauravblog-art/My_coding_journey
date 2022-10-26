# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      
      newnode=ListNode()
      def merge(newnode,lst1,lst2):
        
        if not(lst1) and not(lst2):
          
          return None
        if lst1==None and lst2!=None:
          
          return  lst2
        if lst1!=None and lst2==None:
          
          return  lst1
        if lst1.val>=lst2.val:
          newnode=lst2
          newnode.next=merge(newnode,lst1,lst2.next)
        else:
          newnode=lst1
          newnode.next=merge(newnode,lst1.next,lst2)
        return newnode
      return merge(newnode,list1,list2)
      
        