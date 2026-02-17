# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Time Complexity- O(4 power n. n) Space Complexity- O(h- h is stack space)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        path = []
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
        
        def helper(index,path):
            if index >= len(digits):
                result.append("".join(path))
                return
            
            for char in char_map[digits[index]]:
                path.append(char)
                helper(index + 1, path)
                path.pop()

        helper(0, path)
        return result

s = Solution()
print(s.letterCombinations('48'))