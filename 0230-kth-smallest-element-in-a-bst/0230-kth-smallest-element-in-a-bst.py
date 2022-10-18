# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
      
      self.ans=0
      self.count=0
      
      def inorder(root,k):
        
        if root:
          
          inorder(root.left,k)
          
          self.count+=1
          if self.count==k:
            self.ans=root.val
          inorder(root.right,k)
      inorder(root,k)
      return self.ans