# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
      if not(root):
        return 
      
      queue=[[root]]
      
      ans=[]
      
      while queue:
        
        level=queue.pop(0)
        ans.append([node.val for node in level])
        
        nested_level=[]
        
        for node in level:
          
          if node.left:
            nested_level.append(node.left)
          if node.right:
            nested_level.append(node.right)
        if nested_level:
          queue.append(nested_level)
      return ans[-1][0]