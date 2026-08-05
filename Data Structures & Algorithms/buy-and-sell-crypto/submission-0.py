class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Single-pass greedy: track the lowest price seen so far (best buy point).
        # For each day, first check the profit if selling at today's price against
        # the minimum buy price found up to (but not including) today, then update
        # the running minimum with today's price for future iterations.
        # No need to consider any earlier, higher buy price since the running
        # minimum is always at least as good.
        
        profit = 0
        buy = float('inf')

        for price in prices:
            profit = max(profit, price - buy)
            buy = min(buy, price)

        return 0 if profit < 0 else profit