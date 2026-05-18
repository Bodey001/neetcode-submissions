class Solution:
    """
    PROBLEM: Daily Temperatures
    
    Given an array of integers `temperatures` representing the daily temperatures, 
    return an array `answer` such that `answer[i]` is the number of days you have 
    to wait after the i-th day to get a warmer temperature. 
    
    If there is no future day for which this is possible, keep `answer[i] == 0`.
    
    SOLUTION STRATEGY: Monotonic Decreasing Stack
    
    We use a stack to keep track of temperatures we are still "waiting" to find 
    a warmer day for. The stack will strictly store elements in decreasing order.
    When we encounter a temperature warmer than the one at the top of the stack, 
    we know the "waiting period" for that top day is over. We pop it, calculate 
    the difference in days (indices), and record it in our output array.
    
    Time Complexity: O(n) - Every element is pushed and popped at most once.
    Space Complexity: O(n) - In the worst case (steadily decreasing temperatures), 
                      the stack will hold all elements.
    """
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0 for _ in range(len(temperatures))]


        for i in range(len(temperatures)):

            while stack and stack[-1][1] < temperatures[i]:
                popped = stack.pop()
                
                distance = i - popped[0]
                output[popped[0]] = distance


            # [index, value] pair
            stack.append([i, temperatures[i]])

        return output