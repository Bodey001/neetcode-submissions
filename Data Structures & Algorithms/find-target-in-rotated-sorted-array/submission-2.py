class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search on a rotated sorted array. At every mid, at least one
        # of the two halves (low..mid or mid..high) is guaranteed to be fully
        # sorted, even though the whole array isn't. Detect which half is
        # sorted, then check if target falls within that sorted half's range:
        #   - if yes, search that half
        #   - if no, target must be in the other half, so search there instead
        # Converges when low == high, the index of target (or -1 if absent).
        # Time: O(log n), Space: O(1)

        low, high = 0 , len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[low] <= nums[mid]:      # the left half is sorted
                if nums[low] <= target <= nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:                           # the right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid

        return low if target == nums[low] else -1