# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
      dummy=temp=ListNode()
      
      carry=0
      
      while l1 or l2 or carry:
        
        v1=0
        v2=0
        
        if l1:
          v1=l1.val
          l1=l1.next
        if l2:
          v2=l2.val
          l2=l2.next
        
        s=v1+v2+carry
        carry=s//10
        val=(s)%10 
        
        temp.next=ListNode(val)
        temp=temp.next
        
      return dummy.next
        