class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize output of 1 based on the lenght on nums.
            # for each i in nums, multiply all elements in the output by a nums[i] 
                # then restore the former state of output[i]
        output = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            current_num = output[i]

            # multiply the output by the nums[i]
            output = [x * nums[i] for x in output]

            # restore the old value for numns[i]
            output[i] = current_num
        
        return output