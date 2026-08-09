class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Each row is sorted, and the first element of each row
        # is greater than the last element of the previous row — so the whole
        # matrix is really just one big sorted list split into chunks.
        # Step 1: find which row could contain target (target fits between
        #         that row's first and last values).
        # Step 2: binary search within that row.

        arr = None

        for m in matrix:
            left = m[0]
            right = m[-1]

            if left <= target <= right:
                arr = m
                break  

        if arr is None:
            return False 

        low = 0
        high = len(arr) - 1

        while low < high:
            median = (high + low) // 2

            if target > arr[median]:   
                low = median + 1
            elif target < arr[median]:
                high = median
            else:
                return True

        return arr[low] == target