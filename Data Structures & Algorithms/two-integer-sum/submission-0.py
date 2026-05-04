class Solution:
    # Loop through the array, check for the difference between the target and the element
        # if difference is already stored in the hashmap return their indexes
        # else: store the element and index in key-value pair
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # an hash table to store the differences
        diff_hash = {}

        for i in range(len(nums)):
            difference = target - nums[i]
                    
            if difference in diff_hash:
                return [diff_hash[difference], i]

            diff_hash[nums[i]] = i