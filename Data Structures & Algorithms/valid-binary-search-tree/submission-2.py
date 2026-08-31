# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode], low = float('-inf'), high = float('inf')) -> bool:
        if root is None:
            return True

        if low < root.val < high:
            # if condition is met, recurse into root.left and root.right
            left = self.isValidBST(root.left, low, root.val)
            right = self.isValidBST(root.right, root.val, high)

            if left == True and right == True:
                return True
            else:
                return False
        else:
            return False