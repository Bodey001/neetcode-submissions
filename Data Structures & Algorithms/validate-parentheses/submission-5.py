class Solution:
    def isValid(self, s: str) -> bool:

        # ==========================================
        # ALGORITHM: VALID PARENTHESES
        # ==========================================
        # We can use a stack (LIFO) to store characters. 
        # Iterate through the string by index. 
        # For an opening bracket, push it onto the stack. 
        # If the bracket is a closing type, check for the corresponding 
        # opening bracket at the top of the stack. 
        # If we don't find the corresponding opening bracket, 
        # immediately return false.


        # Method 1:
        stack = []

        bracket_map = {")": "(", "]": "[", "}": "{"}

        if len(s) % 2 != 0:
            return False

        for char in s:
            # Check for top_element in the stack
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'

                if top_element != bracket_map[char]:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0



        # # Method 2:
        # from collections import deque
        # stack = deque()    

        # for bracket in s:
        #     if bracket == '(' or bracket == '{' or bracket == '[':
        #         stack.append(bracket)
        #     elif stack:
        #         if bracket == ')' and stack[-1] == '(':
        #             stack.pop()
        #         elif bracket == ']' and stack[-1] == '[':
        #             stack.pop()
        #         elif bracket == '}' and stack[-1] == '{':
        #             stack.pop()
        #         else:
        #              return False
        #     else:
        #         return False
        
        # return len(stack) == 0