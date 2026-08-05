class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two-pointer approach: start with the widest possible container
        # (left pointer at index 0, right pointer at the last index) and
        # shrink inward.
        #
        # At each step, the container's area is bounded by the SHORTER of
        # the two walls (distance * min(heights[j], heights[k])), since
        # water can't rise above the shorter side.
        #
        # Greedy insight: keeping the shorter wall in place can never
        # produce a larger area later, because any future pairing is
        # limited to a smaller distance AND still capped by that same
        # short wall (or an even shorter one). So it's always safe to
        # discard the shorter wall and move that pointer inward, hoping
        # to find a taller wall to pair with. If the walls are equal,
        # either can be discarded — here we move the right pointer.
        #
        # This explores all "useful" pairs in O(n) time with O(1) space,
        # instead of checking every pair in O(n^2).

        j = 0
        k = len(heights) - 1
        maxArea = 0

        while j < k:
            distance = k - j

            area = distance * min(heights[j], heights[k])
            maxArea = max(area, maxArea)

            if heights[j] < heights[k]:
                j += 1
            else:
                k -= 1

        return maxArea