class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # Approach: hash map + doubly linked list.
    #
    # - The hash map (key -> Node) gives O(1) lookup by key.
    # - The doubly linked list keeps nodes ordered by recency: the
    #   head sentinel side is least recently used, the tail sentinel
    #   side is most recently used.
    # - Dummy head/tail sentinels mean every real node always has a
    #   valid prev/next, so no None-checks are needed when unlinking.
    # - Any time a key is read (get) or written (put), its node is
    #   unlinked from its current spot and reinserted right before
    #   the tail -- that's what "marks it as most recently used".
    # - When put() adds a new key past capacity, the node immediately
    #   after the head sentinel is always the LRU node, so eviction
    #   is a direct removal with no search.
    #
    # Time:  O(1) for both get() and put() -- dict lookup plus a
    #        fixed number of pointer rewires, no scanning.
    # Space: O(capacity) -- one node and one dict entry per cached key.

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node, for O(1) lookup

        self.head = Node()  # LRU side sentinel
        self.tail = Node()  # MRU side sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # unlink node from its current position by rewiring
        # the pointers of the nodes on either side of it
        node.prev.next = node.next
        node.next.prev = node.prev

        # reinsert it just before the tail sentinel --
        # accessing a key counts as using it, so it becomes MRU
        previous_node = self.tail.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.tail
        self.tail.prev = node
        
        return node.val
        

    def put(self, key: int, value: int) -> None:

        # key already cached: update its value and refresh its
        # position, since writing to a key also counts as using it
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            # unlink node from its current position
            node.prev.next = node.next
            node.next.prev = node.prev

            # reinsert it just before the tail sentinel (MRU end)
            previous_node = self.tail.prev
            previous_node.next = node
            node.prev = previous_node
            node.next = self.tail
            self.tail.prev = node
            return

        # new key: if the cache is already at capacity, evict the
        # LRU node -- it always sits right after the head sentinel
        if len(self.cache) >= self.capacity:
            lru = self.head.next
            self.head.next = lru.next
            lru.next.prev = self.head
            del self.cache[lru.key]

        # insert the new node at the tail (MRU end) and track it in the map
        new_node = Node(key, value)
        self.cache[key] = new_node

        previous_node = self.tail.prev
        previous_node.next = new_node
        new_node.prev = previous_node
        new_node.next = self.tail
        self.tail.prev = new_node