class MinStack:
    # ==========================================
    # PROBLEM: MIN STACK
    # ==========================================
    # Design a stack class that supports push, pop, top, and getMin operations.
    # All operations must run in O(1) time.
    # 
    # Operations:
    # - MinStack(): initializes the stack object.
    # - push(int val): pushes the element val onto the stack.
    # - pop(): removes the element on the top of the stack.
    # - top(): gets the top element of the stack without removing it.
    # - getMin(): retrieves the minimum element in the stack without removing it.
    #
    # Constraints:
    # - -2^31 <= val <= 2^31 - 1.
    # - pop, top and getMin will always be called on non-empty stacks.
    #
    # ==========================================
    # SOLUTION: TWO-STACK APPROACH (PREFIX MINIMUM)
    # ==========================================
    # To achieve O(1) time for getMin(), we use an additional stack (min_stack) 
    # to maintain the "prefix minimum" element. 
    # 
    # - Push: When pushing a value onto the main stack, we also push a value 
    #   onto the min_stack. This value is the minimum between the new value 
    #   and the current minimum (which sits at the top of the min_stack).
    # - Pop: When popping from the main stack, we simply pop from the min_stack 
    #   as well to keep their lengths and states perfectly synchronized.
    # - getMin: Because of this synchronization, the current minimum of the 
    #   entire stack is always sitting right at the top of the min_stack.
    # ==========================================

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1])) if self.min_stack else self.min_stack.append(val)
        
        return None

    def pop(self) -> None:
        self.stack.pop() if self.stack else None
        self.min_stack.pop() if self.min_stack else None
        return None
        
    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1
