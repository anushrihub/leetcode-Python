# https://leetcode.com/problems/move-zeroes/
# Time Complexity- O(n) Space Complexity- O(1)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left pointer
        left = 0
        # iterate over the list
        for i in range(len(nums)):
            # if the element is not 0
            if nums[i]!= 0:
                # swap the elements
                nums[i],nums[left] = nums[left], nums[i]
                left += 1
        return nums
            
s = Solution()
print(s.moveZeroes([0,1,0,3,12]))


