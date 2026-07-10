# https://leetcode.com/problems/length-of-last-word/

# Time complexity- O(n) Space Complexity- O(1)

class Solution:
    def lengthOfLastWord(self, s: str):
        # find the lenght
        length = len(s) - 1
        # this edge case handles the condition when last element is blank and we want to find the length of the last word so decrease the length
        while s[length] == ' ':
            length -= 1
        # define the counter
        count = 0
        # run the loop
        for i in range(length, -1, -1):
            # when the character is blank break the loop
            if s[i] == ' ':
                break
            # count will happen as the loop progress
            count += 1
        # return the count
        return count
            



s = Solution()
print(s.lengthOfLastWord('Hello World')) 
# 5
print(s.lengthOfLastWord('  fly me   to   the moon  '))
# 4
# print(s.lengthOfLastWord('luffy is still joyboy'))
# 6