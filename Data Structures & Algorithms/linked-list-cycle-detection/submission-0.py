# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Detect a cycle by tracking which node OBJECTS we've already
        # visited (not their values - two different nodes can share the
        # same value without any cycle existing).
        #
        # Walk the list one node at a time. If we ever reach a node
        # we've already put in `seen`, we must have looped back via a
        # cycle - a normal (acyclic) list can only visit each node once
        # before hitting None.
        #
        # O(n) time, O(n) space for the seen-set.
        seen = set()

        while head is not None:
            if head not in seen:
                seen.add(head)
                head = head.next
            else:
                return True

        return False