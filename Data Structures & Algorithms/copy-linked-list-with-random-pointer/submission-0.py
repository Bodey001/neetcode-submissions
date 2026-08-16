# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Two-pass, dictionary-mapping pattern:
        # 1. Walk the original list once, creating a bare copy (val only)
        #    for every node, and record orig -> copy in a dict. Every
        #    node gets an entry, regardless of what it points to.
        # 2. Walk it again, wiring next and random via dict lookups:
        #    old_to_new.get(x) returns None automatically when x is None,
        #    so null pointers need no special-casing.
        if not head:
            return None

        old_to_new = {}

        # First pass: create every copy node, map orig -> copy
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: wire next and random using the map
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]