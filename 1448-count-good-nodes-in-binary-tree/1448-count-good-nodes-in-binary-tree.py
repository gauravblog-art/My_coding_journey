# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
      self.ans=0
      def solver(root, maxn):
        
        if not root:
          return 
        
        if root.val>=maxn:
          
          self.ans+=1
        
        solver(root.left, max(root.val,maxn))
        solver(root.right, max(root.val,maxn))
        
      solver(root,float('-inf'))
      return self.ans        
        