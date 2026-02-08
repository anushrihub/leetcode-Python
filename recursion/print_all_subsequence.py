# https://leetcode.com/problems/subsets/description/
# Backtracking example
# Time Complexity- O(n * 2 power n) Space Complexity- O(n) + O(n * 2 power n) =  O(n * 2 power n)
class Solution:
    def subsets(self,nums: list):
        # create result set
        res = []
        # create current subset
        sequence = []
        def helper(i):
            # base case
            if i >= len(nums):
                res.append(sequence.copy())
                return
            # choose
            # state of modification
            sequence.append(nums[i])
            # explore with this choice
            helper(i + 1)
            # restore state (backtrack)
            sequence.pop()
             # not choose
            helper( i + 1)
        helper(0)
        return res

s = Solution()
print(s.subsets([3,5]))
