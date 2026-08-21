"""
Merge K Sorted Lists

Approach: Sequential pairwise merging.
Reduce the k-way merge to (k-1) applications of the standard
two-list merge (mergeTwoLists), folding the result of each merge
into the next list in the array:

    head = merge(lists[0], lists[1])
    head = merge(head, lists[2])
    ...
    head = merge(head, lists[k-1])

mergeTwoLists itself uses the classic dummy-node + tail-pointer
pattern: walk both lists with two pointers, always attaching the
smaller current node to tail.next, then advancing both tail and
that list's pointer. When one list runs out, splice in whatever
remains of the other in one shot (no need to walk it node-by-node)
since it's already sorted.

Edge cases handled explicitly:
- lists == []          -> return None (no lists to merge)
- lists has 1 list      -> return it unchanged (nothing to merge)

Time:  O(N*k) where N = total nodes across all lists, k = number of lists
       (each node gets re-visited once per merge it's involved in)
Space: O(1) extra (excluding the output list itself) — nodes are
       relinked in place, not copied
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

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
        
        # One list is exhausted — the other is already sorted,
        # so splice in the remainder wholesale.
        tail.next = list1 if list1 is not None else list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        # elif len(lists) == 1:
        #     return lists[0]

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            
            lists = merged

        return lists[0]