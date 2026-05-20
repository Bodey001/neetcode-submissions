class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        PROBLEM: Car Fleet
        
        There are `n` cars traveling to the same `target` destination along a 
        single-lane road. You are given two arrays: `position` and `speed`.
        
        Rules of the road:
        1. Cars cannot pass each other.
        2. If a faster car catches up to a slower car, they form a "fleet" and 
        continue driving together at the speed of the slower car.
        3. A single car is also considered a fleet.
        
        Goal: Return the total number of car fleets that will arrive at the target.
        
        SOLUTION STRATEGY: Sorting + Stack (Tracking Bottlenecks)
        
        Because cars only interact with those *in front* of them, we process the 
        cars starting from the one closest to the target and work backwards.
        
        1. Pair positions and speeds, then sort descending by position.
        2. Calculate the theoretical Time of Arrival (ETA) for each car as if 
        there were no other cars on the road.
        3. Use a stack to keep track of the ETAs of the fleet leaders. 
        - If a car behind has an ETA <= the fleet ahead, it catches up. It joins 
            the fleet, so we don't add it to the stack (the bottleneck remains).
        - If a car has an ETA > the fleet ahead, it is too slow to catch up. 
            It forms a new fleet, so we push its ETA onto the stack.
            
        Time Complexity: O(n log n) - Dominated by the sorting step.
        Space Complexity: O(n) - For storing the zipped pairs and the stack.
        """
        
        # Merge the arrays and sort them
        pairs = sorted(zip(position, speed), reverse=True)      

        # Calculate the time for each element
        stack = []
        for p, s in pairs:
            current_eta = (target - p) / s
            
            if not stack or current_eta > stack[-1]:
                stack.append(current_eta)

        return len(stack)