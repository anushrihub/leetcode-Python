# https://leetcode.com/problems/group-anagrams/
# Time Complexity- O(m * n log n) Space Complexity- O(m * n) - Same for both solutions

from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs):
#         map = {}

#         for char in strs:
#             sorted_char = "".join(sorted(char))
#             if sorted_char not in map:
#                 map[sorted_char] = []
#             map[sorted_char].append(char)

#         return list(map.values())
                      
class Solution:
    def groupAnagrams(self, strs):
        map = defaultdict(list)
        for char in strs:
            sorted_char = "".join(sorted(char))
            map[sorted_char].append(char)
        return list(map.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))