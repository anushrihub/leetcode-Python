# https://leetcode.com/problems/3sum/description/
# Time Complexity- O(n3) Space Complexity- O(m)

# class Solution:
#     def threeSum(self, nums: list[int]):
#         n = len(nums)
#         # to avoid duplicates but set treats different orders as different values.
#         result = set()
#         # so sorting see every duplicate into the same order and set will remove that
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         tmp = [nums[i], nums[j], nums[k]]
#                         result.add(tuple(tmp))
#         return [list(i) for i in result]

# Time Complexity- O(n2) Space Complexity- O(m)
# m: number of the triplet
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        # sorting the given array
        nums.sort()
        # this is the output space that never count in complexity
        result = []
        # iterating over the array so that 1 number will be fixed out of 3 
        for i in range(n):
            # after 1st number all the element will be positive as we have sorted the array. so breaking the loop because there would be no negative to make the target 0
            if nums[i] > 0:
                break
            # need to skip the duplicate values for the 1st number so checking with precious number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # using two pointers to search on the right array
            low, high = i+1, n-1
            # to make sure two pointers should not cross
            while low < high:
                # add the three numbers to find the triplet
                total = nums[i] + nums[low] + nums[high]
                # if the total is greater than zero, we need to move the right pointer
                if total > 0:
                    high -= 1
                # if the total is smaller than zero, we need to move the left pointer
                elif total < 0:
                    low += 1
                # when total is zero, found the valid 3 numbers
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    # move the pointer
                    low += 1
                    high -= 1
                    # to skip the duplicate value in the two pointers
                    while nums[low] == nums[low - 1] and low < high:
                        low += 1
                
        return result
        
                

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))