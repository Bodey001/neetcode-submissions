# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__ (self):
        self.max_dia = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max_dia   
          
    def depth(self, root):
        if root is None:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        self.max_dia = max(self.max_dia, sum([left_depth, right_depth]))

        return 1 + max(left_depth, right_depth)