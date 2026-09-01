# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.counter = 0
        self.value = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find the kth smallest value in a BST using inorder traversal
        (left -> node -> right), which visits BST nodes in ascending
        sorted order.

        self.counter tracks how many nodes have been visited so far;
        self.value stores the answer once the kth node is reached.

        Two early-stop guards prevent wasted recursion once the answer
        is found:
          - At the top of each call: if self.value is already set,
            return immediately without doing any work in this frame.
          - Right after the left-subtree call: if the left side already
            found the answer, skip this frame's own counter increment
            and skip recursing into the right subtree entirely.

        Without these guards the recursion would still visit every
        node in the tree even after the kth smallest was found.

        Time:  O(h + k) — descends to the leftmost node (h = height),
               then visits k nodes in sorted order before stopping.
        Space: O(h) — recursion stack depth equals tree height.
        """

        if root is None:
            return self.value

        if self.value is not None:
            return self.value

        self.kthSmallest(root.left, k)

        if self.value is not None:
            return self.value

        self.counter += 1
        if self.counter == k:
            self.value = root.val
            return self.value

        self.kthSmallest(root.right, k)

        return self.value