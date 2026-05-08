class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # loop through, save the prefex products into each output slot
            # loop

        output = [1 for _ in range(len(nums))]


        # Prefix loop
        prefix = 1
        for i in range(len(nums)):
            # store the prefix value in output[i]
            output[i] = prefix

            # multiply prefix by nums[i]
            prefix *= nums[i]


        # Suffix loop
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            # multiply output[j] by suffix
            output[j] *= suffix

            suffix *= nums[j]

        return output           