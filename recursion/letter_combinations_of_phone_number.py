# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Time Complexity- O(4 power n. n) Space Complexity- O(h- h is stack space)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        path = []
        # create a dictionary
        char_map = {
                    "2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz"
                    }
        # helper function
        def helper(index,path):
            # base case
            if index >= len(digits):
                result.append("".join(path))
                return
            # use for loop for iteration
            # char_map[digits[0]] - 4
            # for char in 4 - g, h, i
            for char in char_map[digits[index]]:
                # append the char
                path.append(char)
                # call the helper function
                helper(index + 1, path)
                # backtrack
                path.pop()

        helper(0, path)
        return result

s = Solution()
print(s.letterCombinations('48'))