# https://leetcode.com/problems/fibonacci-number/
# Time Complexity- O(2 power n)- function is making two recursive calls everytime.  Space Complexity- O(n - stack space)

class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        # base case
        elif n == 1:
            return 1
        # call the function recursively
        return self.fib(n - 1) + self.fib(n - 2)
    

s = Solution()
print(s.fib(3))