class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach: Sort + Two Pointers (O(n^2) time, O(1) extra space)
        #
        # 1. Sort the array. This groups equal values together (making
        #    duplicate-skipping cheap) and enables the two-pointer scan.
        #
        # 2. Fix one number at index i, turning the problem into finding
        #    two more numbers (right of i) that sum to -nums[i]. This is
        #    a classic two-sum, solved in O(n) with two pointers since
        #    the subarray is sorted.
        #
        # 3. For each i:
        #      - Skip if nums[i] == nums[i-1], to avoid reprocessing the
        #        same fixed value and generating duplicate triplets.
        #      - Set j just after i, k at the end of the array.
        #      - While j < k, compare nums[j] + nums[k] to target:
        #          sum < target -> move j right (need a bigger value)
        #          sum > target -> move k left  (need a smaller value)
        #          sum == target -> record the triplet, then move both
        #            pointers inward AND skip past any further duplicate
        #            values at the new j/k positions, so the same
        #            triplet isn't recorded more than once.
        #
        # Overall: O(n) outer iterations x O(n) inner two-pointer sweep
        # = O(n^2) time; only a constant number of extra variables are
        # used, so O(1) auxiliary space (ignoring the output list).

        nums.sort()

        output = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[j] + nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return output