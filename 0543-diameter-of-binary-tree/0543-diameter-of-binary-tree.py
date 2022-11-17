# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      self.maxi=0
      def solver(root):
        if not root:
          return 0
        left=solver(root.left)
        right=solver(root.right)
        self.maxi=max(self.maxi,left+right)
        # print(maxi)
        return 1+ max(left,right)
      solver(root)
      # print(maxi)
      return self.maxi