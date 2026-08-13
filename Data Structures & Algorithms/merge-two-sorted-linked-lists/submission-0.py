# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Merge two already-sorted linked lists into one sorted list by
        # relinking existing nodes (no new nodes created, no values copied).
        #
        # dummy - a throwaway placeholder node so the first real node
        #         attached doesn't need special-case handling
        # tail  - always points to the last node attached to the result;
        #         starts at dummy, advances by one every time a node
        #         is attached
        #
        # Walk list1 and list2 together. At each step, whichever current
        # node has the smaller value gets attached to tail.next, and only
        # that list's pointer advances - the other list's current node is
        # still un-beaten, so it stays put for the next comparison.
        #
        # Once one list runs out, the other is already sorted, so the
        # remainder is spliced on in a single line instead of looping
        # node by node.
        #
        # O(n + m) time (each node visited once), O(1) space.
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 is not None else list2

        return dummy.next