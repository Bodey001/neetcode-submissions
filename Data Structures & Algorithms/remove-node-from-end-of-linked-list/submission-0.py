# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two-pointer with a gap, dummy-node pattern:
        # 1. Advance `fast` n steps ahead of `slow` (which starts at dummy).
        # 2. Walk both forward together until `fast` falls off the end (None) -
        #    `slow` now sits on the node just before the one to remove.
        # 3. Splice it out unconditionally: slow.next = slow.next.next.
        # Dummy node means "remove the head" needs no special case.
        
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy.next

        for _ in range(n):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next