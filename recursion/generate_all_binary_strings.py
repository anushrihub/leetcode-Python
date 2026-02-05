class Solution:
    def generateBinaryStrings(self, n):
        numbers = ["0"] * n
        result = []
        self.helper(0, True, numbers, result)
        return result


    def helper(self, index, flag, numbers, result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return 
        
        numbers[index] = "1"
        self.helper(index + 1, True, numbers, result)
        if flag == True:
            numbers[index] = "0"    
            self.helper(index + 1, False, numbers, result)
            numbers[index] = "1"

solution = Solution()
print(solution.generateBinaryStrings(2))