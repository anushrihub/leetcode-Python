# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                # Incrementing insertIndex count by 1
                insertIndex = insertIndex + 1
        return insertIndex



s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([1,1,2]))
# o/p : 2