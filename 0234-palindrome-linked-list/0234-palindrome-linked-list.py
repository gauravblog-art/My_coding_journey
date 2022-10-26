# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      
      # find the midle element
      
      slow=head
      fast=head
      while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
      
      node=None
      while slow:
        temp=slow.next
        slow.next=node
        node=slow
        slow=temp
      
      while node:
        
        if head.val!=node.val:
          return False
        head=head.next
        node=node.next
      return True
        