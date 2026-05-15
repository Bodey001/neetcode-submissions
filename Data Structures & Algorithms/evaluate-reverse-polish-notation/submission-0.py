class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ==========================================
        # PROBLEM: EVALUATE REVERSE POLISH NOTATION (RPN)
        # ==========================================
        # Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        # Valid operators are +, -, *, and /. Each operand may be an integer or 
        # another expression.
        #
        # Constraints & Rules:
        # - Division between two integers should truncate toward zero.
        # - The given RPN expression is always valid (no division by zero).
        # - The expression will always evaluate to a single integer.
        #
        # Example: 
        # Input: ["2", "1", "+", "3", "*"]
        # Output: 9
        # Explanation: ((2 + 1) * 3) = 9
        #
        # ==========================================
        # SOLUTION: STACK ALGORITHM 
        # ==========================================
        # RPN is perfectly suited for a Stack (LIFO) because operators 
        # are strictly applied to the two most recently seen numbers.
        #
        # Algorithm Step-by-Step:
        # 1. Iterate through every token in the array.
        # 2. If the token is a number, push it onto the stack.
        # 3. If the token is an operator, pop the top two numbers from the stack.
        #    -> CRITICAL: The first popped number is the RIGHT operand.
        #    -> The second popped number is the LEFT operand.
        # 4. Apply the mathematical operation to these two numbers.
        # 5. Push the resulting calculated integer back onto the stack.
        # 6. Once the loop finishes, the stack will contain exactly one 
        #    element: the final evaluated answer.
        #
        # Time Complexity: O(n) - We visit each token exactly once.
        # Space Complexity: O(n) - The stack stores numbers, up to n/2 in the worst case.
        # ==========================================
        
        import operator
        
        operator_hashmap = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        stack = []

        for token in tokens:
            if token not in operator_hashmap:
                stack.append(int(token))
            else:
                if stack and len(stack) >= 2:
                    right_operand = int(stack.pop())
                    left_operand = int(stack.pop())

                    result = operator_hashmap[token](left_operand, right_operand)
                    stack.append(int(result))
        
        return stack[0]