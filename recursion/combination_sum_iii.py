# https://leetcode.com/problems/combination-sum-iii/description/
# Time Complexity- O(2 power n. k) Space Complexity- O(k)

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        arr = [i for i in range(1,10)]
        result = []
        path = []

        def helper(index, sum, count):
            # base case
            if count == k:
                if sum == n:
                    result.append(path.copy())
                return
            # base condition
            if index >= len(arr) or count > n:
                return
            # append the path
            path.append(arr[index])
            # make the choice and increase the index, sum and count
            helper(index + 1, sum + arr[index], count +1)
            # pop the choice
            path.pop()
            # increase the index
            helper(index + 1, sum, count)

        helper(0, 0, 0)
        return result
    
s = Solution()
print(s.combinationSum3(k = 3, n = 7))
            
        