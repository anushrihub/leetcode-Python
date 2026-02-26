# https://leetcode.com/problems/valid-anagram/description/
# Time Complexity- O(n + m) Space Complexity- O(1)
# n is the length of string s and m is the length of string t
# space is 1 because at most character is 26

class Solution:
    def isAnagram(self, s: str, t: str):
        s_map = {}
        t_map = {}
        if len(s) != len(t):
            return False
        for s_char in s:
            s_map[s_char] = 1 + s_map.get(s_char,0)
        for t_char in t:
            t_map[t_char] = 1 + t_map.get(t_char,0)

        return s_map == t_map

s = Solution()
print(s.isAnagram(s = "iceland", t = "landice"))