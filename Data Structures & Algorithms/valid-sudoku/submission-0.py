class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validates a 9x9 Sudoku board.
        
        Only the filled cells need to be validated according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        
        Algorithm:
        Utilizes three arrays of Hash Sets to track the numbers we have seen so far 
        in each respective row, column, and 3x3 sub-box. As we traverse the grid once, 
        we check for collisions in O(1) time.

        Complexity:
        - Time Complexity: O(1). The board size is fixed at 9x9, resulting in a maximum 
          of 81 iterations. Set lookups and insertions are O(1).
        - Space Complexity: O(1). At most, 81 elements will be stored across the hash sets, 
          which is a constant upper bound.
        """

        # Create 3 hash_set tables
        rows_hash_set = {}
        cols_hash_set = {}
        squares_hash_set = {}
        
        # Initialze the hash tables
        for i in range(1, len(board) + 1):
            rows_hash_set[i] = set()
            cols_hash_set[i] = set()
            squares_hash_set[i] = set()


        for i in range(len(board)):
            for j in range(len(board[i])):
                # check if element is in rows_hash
                element = board[i][j]
                box_index = ((i//3)*3) + (j//3)
            
                if element in rows_hash_set[i+1] and element != ".":
                    return False
                rows_hash_set[i+1].add(element)

                if element in cols_hash_set[j+1] and element != ".":
                    return False
                cols_hash_set[j+1].add(element)

                if element in squares_hash_set[box_index+1] and element != ".":
                    return False
                squares_hash_set[box_index+1].add(element)

        return True