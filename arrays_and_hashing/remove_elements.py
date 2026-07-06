# https://leetcode.com/problems/remove-element/
# Time complexity- O(n) Space Complexity- O(1)

class Solution:
    def removeElement(self, nums: list[int], val: int):
        count = 0
        l = len(nums)


        for i, num in enumerate(nums):
            if num != val:
                nums[count] = num
                count += 1
        return count



s = Solution()
print(s.removeElement([3,2,2,3], 3))
print(s.removeElement([0,1,2,2,3,0,4,2], 2)) 