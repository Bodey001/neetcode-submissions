from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search on the answer: search over possible eating rates k
        # (not over the piles array itself). The search space is [1, max(piles)] —
        # 1 is the slowest possible rate, and max(piles) always finishes every
        # pile within 1 hour each, so it's a guaranteed upper bound.
        #
        # feasible(k) = "can all piles be eaten within h hours at rate k" is
        # monotonic: if a rate works, every faster rate also works. That lets
        # binary search find the smallest working rate instead of checking
        # every value from 1 to max(piles) one by one.
        #
        # For a given mid (candidate rate), total_hours sums ceil(pile/mid)
        # across all piles — ceil because any partial pile still costs a full
        # extra hour. If total_hours > h, mid is too slow, so search higher
        # (low = mid + 1). Otherwise mid works, so record it and search lower
        # for a possibly smaller rate (high = mid, keeping mid in range since
        # it's still a valid candidate).
        #
        # Time: O(n log m), Space: O(1), where n = len(piles), m = max(piles)

        low = 1
        high = max(piles)


        result = high
        while low < high:

            mid = (high + low) // 2             # eating rate
            total_hours = sum(ceil(pile/mid) for pile in piles)     #total_hours based on the eating rate

            if total_hours > h:         # eating rate is too small
                low = mid + 1
            elif total_hours <= h:       # eating rate is feasible (might be too large. check for lower numbers)
                high = mid
                result = min(mid, result)

        return result