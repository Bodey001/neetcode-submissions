# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse a singly linked list in-place by walking it once and
        # flipping each node's .next pointer to point backward instead
        # of forward.
        #
        # Two pointers do the work:
        #   front_next - the node that should come BEFORE curr in the
        #                reversed list (starts as None, since the
        #                original head becomes the new tail, and a
        #                tail's .next is None)
        #   curr       - the node currently being rewired (starts at head)
        #
        # Each iteration: save curr.next before overwriting it (otherwise
        # we lose the rest of the list), point curr backward at
        # front_next, then slide both pointers one node forward.
        #
        # When curr runs off the end (becomes None), front_next is sitting
        # on the last node we rewired - which is the new head. O(n) time,
        # O(1) space.
        front_next = None
        curr = head

        while curr is not None:
            # from the perspective of current
            back_node = curr.next      # remember what's ahead before we overwrite curr.next
            curr.next = front_next     # reverse this node's pointer

            # from the perspective of after current
            front_next = curr          # slide front_next forward
            curr = back_node           # slide curr forward

        return front_next