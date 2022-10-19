# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    
      queue=[root]
      
      while queue:
        
        p=queue.pop(0)
        
        if p.right: queue.append(p.right)
        if p.left: queue.append(p.left)
      return p.val