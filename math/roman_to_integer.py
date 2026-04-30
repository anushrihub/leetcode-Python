# https://leetcode.com/problems/roman-to-integer/

# time complexity- O(n) space complexity- O(1)- keys of map are fixed

class Solution:
    def romanToInt(self, s: str):

        map = { 'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,      
                'D' : 500,
                'M' : 1000}
        
        amount = 0

        for i in range(len(s)):
            # when a smaller value appears before a larger value, it should be subtracted, not added.
            if i+1 < len(s) and map[s[i]] < map[s[i+1]]:
                amount -= map[s[i]]
            else:
                amount += map[s[i]]
        return amount

s = Solution()
print(s.romanToInt('III'))
print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))
