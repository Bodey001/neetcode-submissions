# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__ (self):
        self.counter = 0
        self.value = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return self.value
      
        if self.value is not None:
            return self.value
            
        self.kthSmallest(root.left, k)
        
        self.counter += 1
        if self.counter == k:
            self.value = root.val
            return root.val

        self.kthSmallest(root.right, k)

        return self.value