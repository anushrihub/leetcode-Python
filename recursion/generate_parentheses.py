# https://leetcode.com/problems/generate-parentheses/description/
# Time Complexity- O(2 power n) Space Complexity- O(2n)


class Solution:
    def generateParenthesis(self, n: int):
        # create a list of n 
        brackets = [" "] * (n * 2)
        result = []
        def helper(OpenN, CloseN, index):
            # base condition when open and close brackets equals to n append into the result set
            if OpenN == CloseN == n:
                result.append("".join(brackets))
                return 

            # if open is less than the n
            if OpenN < n:
                # append open paranthesis
                brackets[index] = '('
                # increase the index and open count by 1
                helper(OpenN + 1, CloseN, index + 1)

            # if close is less than the open
            if CloseN < OpenN:
                # append close paranthesis
                brackets[index] = ')'
                # increase the index and open count by 1
                helper(OpenN, CloseN + 1, index + 1)
        # call the function
        helper(0, 0, 0)
        return result


s = Solution()
print(s.generateParenthesis(3))