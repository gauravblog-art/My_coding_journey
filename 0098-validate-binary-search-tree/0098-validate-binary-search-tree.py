# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      
      
      def solver(root,left,right):
        
        if not root:
          return True
        
        if not(left<root.val and right>root.val):
          
          return False
        
        return solver(root.left,left,root.val) and solver(root.right,root.val,right)
      
      return solver(root, float('-inf'), float('inf'))
      