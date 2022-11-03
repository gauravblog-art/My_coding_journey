# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      
      
      self.ans=1
      
      def solver(root):
        
        if not root:
          return 0
        
        left=solver(root.left)
        right=solver(root.right)
        
        if abs(left-right)>1:
          self.ans=0
          
        return 1+max(left,right)
      
      solver(root)
      
      if self.ans==1:
        return True
      
      else:
        return False
          
        
      