# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.output = []

    def goodNodes(self, root: TreeNode, max_value = float('-inf')) -> int:
        if root is None:
            return []

        if root.val >= max_value:
            self.output.append(root.val)
        
        max_value = max(max_value, root.val)

        self.goodNodes(root.left, max_value)
        self.goodNodes(root.right, max_value)

        return len(self.output)