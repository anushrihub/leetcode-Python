# https://leetcode.com/problems/contains-duplicate/description/
# Time Complexity- O(n2) Space Complexity- O(1)
# but this gives time limit exceed, because comparision is in higher count
# class Solution:
#     def containsDuplicate(self, nums: list[int]):
#         for num1 in range(len(nums)):
#             for num2 in range(num1+1,len(nums)):
#                 if nums[num1] == nums[num2]:
#                     return True
#         return False


# Time Complexity- O(n) Space Complexity- O(n)
# class Solution:
#     def containsDuplicate(self, nums: list[int]):
#         n_map = {}
#         for num in nums:
#             if num in n_map:
#                 n_map[num] += 1
#             else:
#                 n_map[num] = 1

#         for val in n_map.values():
#             if val > 1:
#                 return True
#         return False

# Time Complexity- O(n) Space Compelxity- O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]):
        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False


s = Solution()
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,2,3,1]))