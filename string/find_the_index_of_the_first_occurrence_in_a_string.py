# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Time complexity- O(n) Space Complexity- O(1)

class Solution:
    def strStr(self, haystack: str, needle: str):
        n = len(needle)
        h = len(haystack)

        for i in range(h):
            if haystack[i:i+n] == needle:
                return i
        return -1





                
s = Solution()
print(s.strStr('leetcode','code'))

