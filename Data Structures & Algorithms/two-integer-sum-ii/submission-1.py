class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        PROBLEM: Two Sum II - Input Array Is Sorted
        
        Given a 1-indexed array of integers `numbers` that is already sorted in 
        non-decreasing order, find two numbers such that they add up to a specific 
        `target` number. Return the indices of the two numbers (1-indexed) as an 
        integer array of size 2. There is exactly one valid solution, and you may 
        not use the same element twice.
        
        SOLUTION STRATEGY: Two Pointers (In-Place)
        
        Because the array is already sorted, we can leverage magnitude. We place 
        one pointer at the start (left) and one at the end (right). We sum the values 
        at these pointers. If the sum is greater than our target, we know our right 
        value is too large, so we decrement the right pointer. If the sum is less 
        than our target, our left value is too small, so we increment the left pointer. 
        We repeat this loop until the exact target is found.
        
        Time Complexity: O(n) - We traverse the array at most once.
        Space Complexity: O(1) - We evaluate the array strictly in-place.
        """
        
        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return[left+1, right+1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
            
                
        return []