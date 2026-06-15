# https://leetcode.com/problems/concatenation-of-array/description/
# time complexity- O(n) space complexity- O(n)

class Solution:
    def getConcatenation(self, nums: list[int]):

        output = []

        # print(output)
        for i in range(len(nums)):
            output.append(nums[i])
        
        for i in range(len(nums)):
            output.append(nums[i])

        return output
            

s = Solution()
print(s.getConcatenation([1,2,1]))

        