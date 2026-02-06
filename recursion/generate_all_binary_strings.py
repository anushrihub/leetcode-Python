        # when flag = True, means previous position was 1, can place 0
        # when flag = False, means previous position was 0, can't place 1
class Solution:
    def generateBinaryStrings(self, n):
        # numbers in the string
        numbers = ["0"] * n
        # result set
        result = []
        # call the helper function
        self.helper(0, True, numbers, result)
        return result


    def helper(self, index, flag, numbers, result):
        # base case
        if index >= len(numbers):
            # join the numbers as a string
            result.append("".join(numbers))
            return 
        # assign 1 to the first index at the created array
        numbers[index] = "1"
        # call the helper function move the index
        # set the flag true
        self.helper(index + 1, True, numbers, result)
        # if the flag is true
        if flag == True:
            # can add the '0'
            numbers[index] = "0"    
            # call the helper function 
            # set the flag False because element after zero should not be the 0
            self.helper(index + 1, False, numbers, result)
            # add 1
            numbers[index] = "1"

solution = Solution()
print(solution.generateBinaryStrings(2))