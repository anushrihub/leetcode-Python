# https://leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x: int):
        # the first case x < 0: to handle the negative numbers
        # second case x % 10 == 0 and x != 0: to handle the numbers which are ending with 0's because if number is ending with zero, then to be palindrome it should start with the 0 and the number should not be the zero
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revertedNumber = 0

        while x > revertedNumber:
            revertedNumber =  revertedNumber*10  + (x % 10)
            x //= 10
        #  x == revertedNumber // 10: to handle the odd length of the number 
        return x == revertedNumber or x == revertedNumber // 10


s = Solution()
print(s.isPalindrome(121))