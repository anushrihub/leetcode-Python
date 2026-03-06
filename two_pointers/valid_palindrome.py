# https://leetcode.com/problems/valid-palindrome/
# Time Complexity- O(n) Space Complexity- O(1)

class Solution:
    def isPalindrome(self, s: str):
        l = 0
        r = len(s) - 1

        while l < r :
            # isalnum checks whether char is alphabet or numeric. if it is not alphanumeric then increment. This step is for removing non-alphanumeric characters
            while l < r and s[l].isalnum() == False:
                l += 1
            # isalnum checks whether char is alphabet or numeric. if it is not alphanumeric then decrement
            while l < r and s[r].isalnum() == False:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))