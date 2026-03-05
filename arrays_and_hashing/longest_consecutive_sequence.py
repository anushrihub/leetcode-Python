# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Time Complexity- O(n2) Space Complexity- O(n)

# it gives time limit exceeded
# class Solution:
#     def longestConsecutive(self, nums: list[int]):
#         n = len(nums)
#         result = 0
#         # create a set to remove the duplicate
#         numset = set(nums)

#         for num in nums:
#             curr = num
#             streak = 0
#             while curr in numset:
#                 # increase it by 1 
#                 curr+= 1
#                 # increase the streak by 1 if the next number is present
#                 streak += 1
#             # check the existing with the newly form streak
#             result = max(streak, result)
#         return result         

# Time Complexity- O(n) Space Complexity- O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]):
        longest = 0
        curr = 0
        # create a set to remove the duplicate
        numset = set(nums)
        for num in numset:
            # check if num - 1 is present in the set or not
            if (num-1) not in numset:
                # if not the length will be starting from the current num
                length = 1
                # check whether the next element is present in set
                while (num + length) in numset:
                    length += 1
                # take the longest sequence
                longest = max(length,longest )
        return longest      

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
        