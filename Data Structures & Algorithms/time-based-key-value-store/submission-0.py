class TimeMap:

    def __init__(self):
        # Maps each key to a list of [value, timestamp] pairs, appended in the
        # order set() is called. Since timestamps arrive non-decreasing per key,
        # each key's list stays sorted by timestamp for free.
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # O(1) amortized: just append to that key's list.
        if key not in self.hash_map:
            self.hash_map[key] = [[value, timestamp]]
        else:
            self.hash_map[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # Binary search for the rightmost entry whose timestamp <= target.
        # Since we keep mid in range on the feasible branch (low = mid, not
        # mid + 1), mid must round UP toward high — otherwise when low and
        # high are adjacent, mid keeps landing back on low and neither
        # pointer moves, causing an infinite loop. (low + high + 1) // 2
        # fixes that by biasing the division upward.
        # Time: O(log n) per get, where n = number of timestamps for that key.

        if key not in self.hash_map:
            return ""
        
        arr = self.hash_map[key]

        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high + 1) // 2

            if arr[mid][1] <= timestamp:
                low = mid
            else:
                high = mid - 1

        return arr[low][0] if arr[low][1] <= timestamp else ""