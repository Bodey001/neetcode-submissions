class Solution:
    def reverseList(self, list1):
        front_next = None
        curr = list1

        while curr is not None:
            back_node = curr.next
            curr.next = front_next
            front_next = curr
            curr = back_node
        
        return front_next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while head is not None:
            # Check whether a full group of k nodes exists starting at head,
            # without consuming head itself yet.
            fast = head
            count = 0
            while fast is not None and count < k:
                fast = fast.next
                count += 1

            if count < k:
                # Fewer than k nodes remain — attach the rest as-is, unreversed,
                # and we're done.
                tail.next = head
                break

            # A full group exists — extract exactly k nodes into headTemp.
            headTemp = ListNode()
            temp = headTemp

            while head is not fast:
                temp.next = head
                head = head.next
                temp = temp.next

            temp.next = None

            rev = self.reverseList(headTemp.next)

            while rev is not None:
                tail.next = rev
                tail = tail.next
                rev = rev.next

        return dummy.next