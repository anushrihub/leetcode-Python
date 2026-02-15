# https://leetcode.com/problems/combination-sum/description/
# Time Complexity- O(2 power n * k) Space Complexity- O(h)- stack space


class Solution:
    def combinationSum(self, candidates, target):
        # define result set
        result = []
        # define path to store the combination and then store the combination into the path
        path = []

        # define the helper function
        # index = to iterate through the given candidates, path = to store the combination, sum = current sum with the given target
        def helper(index, path, sum):
            # base condition
            if sum == target:
                # append the copy of path into the result
                result.append(path.copy())
                return

            # base condition
            if sum > target or index >= len(candidates):
                return

            # value at the index
            candidates[index]
            # add the value into the path
            path.append(candidates[index])
            # call the function with the same index as we can choose same value multiple times and increase the sum by adding the value
            helper(index, path, sum + candidates[index])
            # backtrack - pop the value
            path.pop()
            # increase the index
            helper(index + 1, path, sum)

        # call the function
        helper(0, path, 0)
        # return the result
        return result


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
