# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time Complexity- O(n) Space Complexity- O(1)

# You can complete at most ONE transaction
# One transaction with maximum profit = buy once + sell once 

    
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # track lowest buy price
            min_price = min(min_price, price)            
            # compare with current sell
            max_profit = max(max_profit, price - min_price)  

        return max_profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))