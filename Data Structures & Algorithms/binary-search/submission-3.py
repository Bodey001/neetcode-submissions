class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:
            
            median = (high + low) // 2
            
            if target <= nums[median]:
                high = median
            else:
                low = median + 1
            

        return low if nums[low] == target else - 1