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

        