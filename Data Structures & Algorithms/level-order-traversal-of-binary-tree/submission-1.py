# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__ (self):
        self.counter = -1
        self.output = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return self.output

        self.counter += 1
        if len(self.output) == self.counter:
            self.output.append([])

        self.output[self.counter].append(root.val)

        self.levelOrder(root.left)
        self.levelOrder(root.right)
        self.counter -= 1

        return self.output