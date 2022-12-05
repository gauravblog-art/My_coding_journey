# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
      
      count=0
      temp=head
      while temp:
        
        count+=1
        temp=temp.next
      if count==1:
        return None
      if count==2:
        head.next=None
        return head
      
      cur=head
      n=count//2
      for i in range(n-1):
        cur=cur.next
      
      cur.next=cur.next.next
      
      return head
     