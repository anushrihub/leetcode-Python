# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Time Complexity- O(n) Space Complexity- O(1)

# You can complete AS MANY transactions as you want
# But you must sell before you buy again
# Maximize total profit from multiple buy–sell pairs

# for loop based
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        r = 1
        total_profit = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                total_profit += prices[i+1] - prices[i]

        return total_profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,2,3,4,5]))


        