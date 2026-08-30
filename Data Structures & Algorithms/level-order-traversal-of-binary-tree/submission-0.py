# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__ (self):
        self.output = []

    def levelOrder(self, root: Optional[TreeNode], counter = -1) -> List[List[int]]:
        if root is None:
            return self.output

        counter += 1
        if len(self.output) == counter:
            self.output.append([])

        self.output[counter].append(root.val)

        self.levelOrder(root.left, counter)
        self.levelOrder(root.right, counter)

        return self.output