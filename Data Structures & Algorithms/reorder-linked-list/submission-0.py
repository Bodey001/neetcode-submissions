# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Reorder in place, three phases:
        # 1. Find the midpoint with slow/fast pointers, split into list1 (first half)
        #    and list2 (second half) — list1 gets the extra node if length is odd.
        # 2. Reverse list2 so it can be merged front-to-back.
        # 3. Merge list1 and reversed list2 by alternating one node from each.
        # Since list1 = head, mutating .next pointers mutates the original list
        # directly — no new head needs to be returned.

        slow = head
        fast = head

        # 1. find the midpoint and separate into two lists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        list1 = head
        list2 = slow.next
        slow.next = None

        # 2. reverse list2
        front_next = None
        curr = list2

            # building the list from the back 
        while curr is not None:
            back_next = curr.next
            curr.next = front_next

            front_next = curr
            curr = back_next

        reverse_list2 = front_next

        # 3. iterate through list1 and reverse_list 2 and merge
        dummy = ListNode()
        tail = dummy
        last_picked = None

        while list1 is not None and reverse_list2 is not None:
            if last_picked is None or last_picked == 2:
                tail.next = list1
                list1 = list1.next
                last_picked = 1
            else:
                tail.next = reverse_list2
                reverse_list2 = reverse_list2.next
                last_picked = 2

            tail = tail.next

        tail.next = list1 if list1 is not None else reverse_list2

        new_head = dummy.next

        return None