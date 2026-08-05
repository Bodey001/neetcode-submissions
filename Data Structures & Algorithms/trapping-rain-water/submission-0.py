class Solution:
    def trap(self, height: List[int]) -> int:
        # ---------------------------------------------------------------
        # Two-Pointer Approach — O(n) time, O(1) space
        #
        # Water trapped at any index i is bounded by:
        #     min(leftMax(i), rightMax(i)) - height[i]
        # where leftMax(i) = tallest bar to the left of (or at) i,
        #       rightMax(i) = tallest bar to the right of (or at) i.
        #
        # Instead of precomputing full leftMax/rightMax arrays (O(n) space),
        # we walk two pointers `l` and `r` inward from both ends, tracking
        # the running max seen so far on each side (`left_max`, `right_max`).
        #
        # Key insight: whichever side has the SMALLER running max is the
        # side we can safely resolve right now. If left_max < right_max,
        # then no matter what lies between l and r, there is already a
        # wall of height right_max (or taller) somewhere to the right —
        # so the water level at position l is capped by left_max alone.
        # We don't need to know the exact right_max at that position,
        # only that it's >= left_max. The same logic applies symmetrically
        # when right_max <= left_max.
        #
        # This lets us move the pointer on the shorter side inward one
        # step at a time, updating that side's running max and adding
        # (running_max - height[pointer]) to the total trapped water,
        # until the two pointers meet.
        # ---------------------------------------------------------------

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        water = 0

        while l < r:
            if left_max < right_max:
                # Left side is the limiting wall — safe to resolve water here
                l += 1
                left_max = max(left_max, height[l])
                water += left_max - height[l]
            else:
                # Right side is the limiting wall (or equal) — resolve here
                r -= 1
                right_max = max(right_max, height[r])
                water += right_max - height[r]

        return water