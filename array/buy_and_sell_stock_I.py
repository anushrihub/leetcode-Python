# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time Complexity- O(n) Space Complexity- O(1)

# You can complete at most ONE transaction
# One transaction with maximum profit = buy once + sell once 

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))