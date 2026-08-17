# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: simulate elementary-school column addition, digit by digit,
        # carrying into the next position when a sum exceeds 9.
        #
        # - Dummy head + tail pointer to build the result list cleanly.
        # - Phase 1: walk l1 and l2 together while both still have nodes.
        # - Phase 2: once one list runs out, keep walking the other alone,
        #   still propagating any leftover carry.
        # - Phase 3: if a carry remains after both lists are exhausted,
        #   append one final node for it.
        #
        # Time:  O(max(m, n)) - each node in both lists visited once
        # Space: O(max(m, n)) - result list length, no extra structures

        # Both lists empty -> no digits to add at all
        if l1 is None and l2 is None:
            return None

        dummy = ListNode()
        tail = dummy
        carry = None

        # Phase 1: add digit-by-digit while both lists still have nodes
        while l1 is not None and l2 is not None:
            num_sum = l1.val + l2.val if carry is None else l1.val + l2.val + carry

            if num_sum > 9:
                tail.next = ListNode(num_sum - 10)
                carry = 1
            else:
                tail.next = ListNode(num_sum)
                carry = None
            
            l1 = l1.next
            l2 = l2.next
            tail = tail.next  # advance tail to the node we just built

        # Phase 2: one list ran out first, keep propagating carry through the rest
        l3 = l1 if l1 is not None else l2
        while l3 is not None:
            num_sum = l3.val if carry is None else l3.val + carry

            if num_sum > 9:
                tail.next = ListNode(num_sum - 10)
                carry = 1
            else:
                tail.next = ListNode(num_sum)
                carry = None
            
            l3 = l3.next
            tail = tail.next

        # Phase 3: both lists exhausted but a carry is still left over
        if carry is not None:
            tail.next = ListNode(carry)

        return dummy.next