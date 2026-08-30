# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Approach:
        Use the BST property (left < node < right) to avoid searching both subtrees.
        At each node, compare p.val and q.val against root.val:
          - both smaller  -> LCA must be in the left subtree, recurse left
          - both larger   -> LCA must be in the right subtree, recurse right
          - otherwise     -> p and q split here (or root is p or q) -> root is the LCA

        Time:  O(h), h = height of the tree (single path down, not a full traversal)
        Space: O(h), recursion stack (O(1) if converted to an iterative loop)
        """
        if p.val < root.val and q.val < root.val:
            lca = self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            lca = self.lowestCommonAncestor(root.right, p, q)
        else:
            lca = root
        
        return lca