# https://leetcode.com/problems/two-sum/description/
# Time Complexity- O(n2) Space Complexity- O(1)

# class Solution:
#     def twoSum(self, nums: list[int], target: int):
#         for num1 in range(len(nums)):
#             for num2 in range(num1 + 1, len(nums)):
#                 if nums[num1] + nums[num2] == target:
#                     return [num1,num2]

# Time Complexity- O(n) Space Complexity- O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int):
        map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [i, map[diff]]
            map[num] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))

        