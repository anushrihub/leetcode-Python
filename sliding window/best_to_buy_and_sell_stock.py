# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Time Complexity- O(n2) Space Complexity- O(1)

# class Solution:
#     def maxProfit(self, prices: list[int]):
#         res= 0 
#         for i in range(len(prices)):
#             buy = prices[i]

#             for j in range(i+1, len(prices)):
#                 sell = prices[j]
#                 res = max(res, sell - buy)
#         return res

# l and r is a window over the array
# Time Complexity- O(n) Space Complexity- O(1)
class Solution:
    def maxProfit(self, prices: list[int]):
        l = 0
        r = 1
        maxp = 0

        while r < len(prices):
            # if the first day value is less than second day
            if prices[l] < prices[r]:
                # it's a profit
                profit = prices[r] - prices[l]
                # update
                maxp = max(maxp, profit)
            # else increment the value
            else:
                l += 1
            # keep incrementing the second pointer
            r += 1

        return maxp

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))