# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      
      # itrative node
      
      stack=[(p,q)]
      
      while stack:
        
        root1,root2=stack.pop()
        
        if not(root1) and not(root2):
          continue
        elif None in [root1,root2]:
          return False
        else:
          
          if root1.val!=root2.val:
            
            return False
          stack.append((root1.right,root2.right))
          stack.append((root1.left,root2.left))
      return True
        
        
      
      
        