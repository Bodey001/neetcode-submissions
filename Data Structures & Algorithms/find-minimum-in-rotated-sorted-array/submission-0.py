class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search for the rotation point in a rotated sorted array
        # (no duplicates, per problem constraints).
        # Compare nums[mid] to nums[high]:
        #   - nums[mid] < nums[high]  -> right half (mid..high) is sorted,
        #     so the minimum is at mid or somewhere to its left -> high = mid
        #   - nums[mid] >= nums[high] -> the "break" in sorted order is
        #     somewhere in (mid, high], so the minimum is past mid -> low = mid + 1
        # Converges when low == high, which is the index of the minimum value.
        # Time: O(log n), Space: O(1)

        low = 0
        high = len(nums) - 1

        while low < high:
            
            mid = (low + high) // 2

            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1

        return nums[low]