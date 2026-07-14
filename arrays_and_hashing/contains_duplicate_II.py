# https://leetcode.com/problems/contains-duplicate-ii/

# it gives time limit exceed
# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int):
#         # seen = {}
#         n = len(nums)

#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] == nums[j] and abs(i - j) <= k:
#                     return True
#         return False

# Time Complexity- O(n) Space Complexity- O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int):
        hmap = {}

        for index, number in enumerate(nums):
            if number in hmap and index - hmap[number] <= k:
                return True
            hmap[number] = index
        return False



            
s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))