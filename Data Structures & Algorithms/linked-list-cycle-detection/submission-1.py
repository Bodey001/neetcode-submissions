# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Two pointers walk the list at different speeds. If there's no
        # cycle, fast reaches None before slow catches up to anything.
        # If there IS a cycle, fast eventually laps slow inside the loop -
        # the gap between them shrinks by exactly 1 node every step (fast
        # gains 2, slow gains 1), so they're guaranteed to land on the
        # same node eventually.
        #
        # O(n) time, O(1) space - no extra data structure needed.
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next        # advance from slow's own position
            fast = fast.next.next   # advance from fast's own position

            if slow is fast:
                return True

        return False  