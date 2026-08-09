class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Standard binary search on a sorted array.
        # Invariant: the answer, if it exists, always lies within nums[low..high] (inclusive).
        # Each iteration halves the search space by comparing target to the midpoint value:
        #   - target > nums[median]  -> answer must be to the right, so low = median + 1
        #   - target < nums[median]  -> answer must be to the left or at median, so high = median
        #   - target == nums[median] -> found it, return immediately
        # Loop runs while low < high, so it narrows down to a single index (low == high).
        # Time: O(log n), Space: O(1)

        low = 0
        high = len(nums) - 1

        while low < high:
            
            median = (high + low) // 2
            
            if target > nums[median]:
                low = median + 1
            elif target < nums[median]:
                high = median
            else:
                return median


        return low if nums[low] == target else -1