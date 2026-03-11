# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time Complexity- O(n * m) Space Complexity- O(m)
# m: total number of unique characters

# class Solution:
#     def lengthOfLongestSubstring(self, s: str):
#         # store the length
#         res = 0

#         # iterate through the string
#         for i in range(len(s)):
#             # create a set to find the duplicate while iterating
#             charset = set()
#             # iterate from the ith element to find the longest substring
#             for j in range(i, len(s)):
#                 if s[j] in charset:
#                     break
#                 charset.add(s[j])
#             res = max(res, len(charset))
#         return res
            

# Time Complexity- O(n) Space Complexity- O(m)
# m: total number of unique characters

class Solution:
    def lengthOfLongestSubstring(self, s: str):
        # create a set
        charSet = set()
        # left pointer
        l = 0
        # result
        res = 0
        # iterate through the string
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l +1)
        return res


        



s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
        