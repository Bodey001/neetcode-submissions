from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            counter = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                counter -= 1

                if counter == 0:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
                