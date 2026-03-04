# https://leetcode.com/problems/product-of-array-except-self/description/

# Time Complexity- O(n2) Space Complexity- O(n)
# Brutforce
# class Solution:
#     def productExceptSelf(self, nums: list[int]):
#         n = len(nums)
#         result = [0] * n
        
#         for i in range(n):
#             prod = 1
#             for j in range(n):
#                 if i == j:
#                     continue
#                 prod *= nums[j]

#             result[i] = prod
#         return result

# Time Complexity- O(n) Space Complexity- O(n)
class Solution:
    def productExceptSelf(self, nums: list[int]):
        running_prod = 1
        n = len(nums)
        result = [0] * n
        result[0] = 1

        # finding the left side sum
        for i in range(1, n):
            # finding the left side product for current element so taking till i - 1
            running_prod *= nums[i-1]
            # append the sum 
            result[i] = running_prod
        
        # finding the right side sum
        # we are finding the sum from the second last element because there is no right side for the last element and this range starts from the 0 so 4 - 2 = 2 (0, 1, 2)
        running_prod = 1
        # stop is exclusive so if we take -1,it will stop at 0
        for i in range(n-2, -1 ,-1):
            # finding the right side product for current element so taking from i + 1
            running_prod *= nums[i + 1]
            
            # multipy the newly formed sum to the exisitng sum
            result[i] = running_prod * result[i]

        # return the result
        return result
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))