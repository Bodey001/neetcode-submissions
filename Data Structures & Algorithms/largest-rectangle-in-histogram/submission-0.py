class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        """
        =======================================================================
        PROBLEM: LARGEST RECTANGLE IN HISTOGRAM
        =======================================================================
        Given an array of integers `heights` representing a histogram where 
        the width of each bar is 1, return the area of the largest rectangle 
        that can be formed within the bounds of the histogram.

        Example:
        Input: heights = [2, 1, 5, 6, 2, 3]
        Output: 10
        Explanation: The largest rectangle is found between indices 2 and 3 
                    (heights 5 and 6). The rectangle is limited by the shorter 
                    height (5) and spans a width of 2, yielding an area of 10.

        =======================================================================
        SOLUTION STRATEGY: THE MONOTONIC INCREASING STACK
        =======================================================================
        To find the maximum rectangle, we must test every bar as if it were 
        the *shortest* bar in a potential rectangle. The area of this rectangle 
        is determined by how far it can expand left and right before hitting 
        a shorter bar. 

        Area = height[i] * (right_boundary_index - left_boundary_index - 1)

        Instead of manually scanning left and right for every single bar (which 
        would take O(n^2) time), we can find both boundaries simultaneously 
        in O(n) time using a Monotonic Increasing Stack.

        DATA STRUCTURE:
        - We use a stack to store the **indices** of the bars, not the heights.
        - INVARIANT: The heights of the bars corresponding to the indices in 
        the stack must be strictly increasing from bottom to top.

        ALGORITHM LOGIC:
        1. The Right Boundary (The Trigger):
        As we loop through the array, if we encounter a bar that is *shorter* 
        than the bar at the top of the stack, it breaks our increasing rule. 
        This shorter bar acts as the exact "Right Boundary" for the stack's top. 

        2. The Left Boundary (The Cascade):
        When we pop the top of the stack to calculate its area, the element 
        sitting immediately below it in the stack is guaranteed to be the 
        first shorter bar to its left. This is its "Left Boundary".

        3. The Base Case (Dummy Index):
        We initialize the stack with `-1`. This acts as a universal Left 
        Boundary for any bar that can successfully extend all the way to 
        the very start of the histogram without hitting a shorter bar.

        4. Flushing the Stack:
        After finishing the loop, any indices remaining in the stack have 
        no shorter bars to their right. Their Right Boundary extends to the 
        very end of the array (represented by the length of the array). 
        We pop them and calculate their final areas.

        COMPLEXITY:
        - Time Complexity: O(n). Despite the nested while loop, every index 
        is pushed onto the stack exactly once and popped at most once.
        - Space Complexity: O(n) to maintain the stack.
        """

        stack = [-1]
        max_area = 0

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:

                current_height = heights[stack.pop()]

                current_width = i - stack[-1] - 1

                max_area = max(max_area, current_height * current_width) 

            
            stack.append(i)
        
        while stack[-1] != -1:
            current_height = heights[stack.pop()]

            current_width = len(heights) - stack[-1] -1

            max_area = max(max_area, current_height * current_width)

        return max_area