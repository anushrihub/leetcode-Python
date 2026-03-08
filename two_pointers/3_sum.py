# https://leetcode.com/problems/3sum/description/
# Time Complexity- O(n3) Space Complexity- O(m)

class Solution:
    def threeSum(self, nums: list[int]):
        n = len(nums)
        # to avoid duplicates but set treats different orders as different values.
        result = set()
        # so sorting see every duplicate into the same order and set will remove that
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        result.add(tuple(tmp))
        return [list(i) for i in result]


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))