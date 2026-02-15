# https://leetcode.com/problems/combination-sum-ii/

# Time Complexity- O(n . 2 power n) Space Complexity- O(n)

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []
        # sort the given list if the next integer is same as before skip it to reduce duplicacy
        candidates.sort()
        
        def helper(index, sum, path):
            # base case
            if sum == target:
                result.append(path.copy())
                return
            
            # base case
            if sum > target or index >= len(candidates):
                return
            
            # index to append
            candidates[index]
            # append the path
            path.append(candidates[index])
            # call the function
            helper(index + 1, sum + candidates[index], path)
            # undo the choice
            path.pop()
            # while indices are still in candidates range and current element is same as the next element
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                # increase the index
                index += 1
            # call the function
            helper(index + 1, sum, path)
        
        helper(0, 0, path)
        return result
    

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))