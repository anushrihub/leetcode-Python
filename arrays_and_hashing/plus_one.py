# https://leetcode.com/problems/plus-one/
# Time complexity- O(n) Space Complexity- O(1)
class Solution:
    def plusOne(self, digits: list[int]):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
            
        
s = Solution()
print(s.plusOne([1,2,3]))
# [1,2,4]
print(s.plusOne([9]))
# [1,0]