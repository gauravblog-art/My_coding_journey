# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
      
      ans=[]
      
      def solver(root):
        
        if not root:
          
          return 
        
        ans.append(str(root.val))
        if root.left==None and root.right==None:
          return 
        
        ans.append('(')
        
        solver(root.left)
        
        ans.append(")")
        
        if root.right:
          ans.append('(')
          solver(root.right)
          ans.append(')')
          
      solver(root)
      
      return ''.join(ans)
        
        
        
        
        
        
        