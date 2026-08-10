class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:
            
            median = (high + low) // 2
            
            if target > nums[median]:
                low = median + 1
            elif target < nums[median]:
                high = median - 1
            else:
                return median


        return -1