class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat the matrix as one flattened sorted array of length m*n.
        # Binary search over indices 0..m*n-1, converting each mid index
        # back into (row, col) via divmod. Since matrix[i][-1] < matrix[i+1][0]
        # for all i, this ordering is valid.
        # Time: O(log(m*n)), Space: O(1)

        if not matrix or not matrix[0]:
            return False

        m , n = len(matrix), len(matrix[0])
        low = 0
        high = (m*n) - 1

        while low < high:
            mid = (high + low) // 2
            mid_val = matrix[mid // n][mid % n]

            if target <= mid_val:
                high = mid
            else:
                low = mid + 1

        return matrix[low // n][low % n] == target