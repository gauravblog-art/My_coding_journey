# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      
    
      def solver(sum_ , root):
        
        if not root:
          return 0
      
        sum_=sum_*10+root.val
        if not(root.left) and not(root.right):
          return sum_
          
        return solver(sum_,root.left) + solver(sum_, root.right)
      
      return solver(0,root)