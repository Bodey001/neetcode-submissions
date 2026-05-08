class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Space Complexity: O(1) auxiliary space (excluding the output array).
        # 
        # Algorithm approach:
        # 1. Prefix Pass (Left to Right): Iterate through the array and calculate the running product 
        #    of all elements to the left of the current index, storing it directly in the output array.
        # 2. Suffix Pass (Right to Left): Iterate backward using a single variable to track the 
        #    running product of all elements to the right. Multiply this running suffix by the 
        #    existing value in the output array to get the final result.

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