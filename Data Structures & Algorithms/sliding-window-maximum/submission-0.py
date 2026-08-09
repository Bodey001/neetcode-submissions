class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Problem: return the max of every size-k window as it slides left to right.
        #
        # Approach: monotonic decreasing deque of INDICES (not values).
        # Invariant: nums[dq[0]] >= nums[dq[1]] >= ... >= nums[dq[-1]] at all times,
        # so the current window's max is always nums[dq[0]].
        #
        # - Before pushing i, pop smaller values off the back: they can never be
        #   the answer again once a bigger value shows up after them, since the
        #   bigger one is both larger and outlasts them in the window.
        # - Pop from the front when dq[0] falls outside the window (i - k).
        #
        # Time: O(n) - each index is pushed once and popped at most once.
        # Space: O(k) - deque holds at most k indices.
        dq = deque()   # stores indices, values decreasing front to back
        result = []

        for i, num in enumerate(nums):
            # pop smaller values off the back — they're now useless
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)

            # drop the front if it's fallen out of the window
            if dq[0] <= i - k:
                dq.popleft()

            # window is full once we've processed k elements
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result