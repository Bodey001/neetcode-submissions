# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            if root1 is None and root2 is not None:
                return False
            elif root1 is not None and root2 is None:
                return False
        elif root1.val != root2.val:
            return False
        
        left = self.sameTree(root1.left, root2.left)
        right = self.sameTree(root1.right, root2.right)

        if left != right:
            return False
        
        return left
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            if root is None and subRoot is not None:
                return False
            elif root is not None and subRoot is None:
                return False
        elif root.val == subRoot.val:
            value = self.sameTree(root, subRoot)
            if value == True:
                return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        if left == True or right == True:
            return True

        return False