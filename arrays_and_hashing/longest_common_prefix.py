# https://leetcode.com/problems/longest-common-prefix/description/

# Time complexity- O(m * n) where n = number of strings, m = length of shortest string
# Space Complexity- O(m) where m is the length of the shortest string

class Solution:
    def longestCommonPrefix(self, strs: list[str]):
        prefix = ''

        for char_index in range(len(strs[0])):
            # print(strs[0][char])
            for n_word_index in range(1, len(strs)):
                # checking the condition if first words index is greater than the length of the word then return the prefix or
                # if first words char is not equal to other words that index then return the prefix
                if char_index >= len(strs[n_word_index]) or strs[0][char_index] != strs[n_word_index][char_index]:
                    return prefix
            # add the first words character to the prefix
            prefix += strs[0][char_index]
        
        return prefix


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
# fl
print(s.longestCommonPrefix(["dog","dog","dog"]))
# 