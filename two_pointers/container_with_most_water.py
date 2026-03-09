# https://leetcode.com/problems/container-with-most-water/description/

# Time complexity- O(n2) Space Complexity- O(1)
# class Solution:
#     def maxArea(self, height):
#         res = 0
#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 res = max(res, min(height[j] ,height[i]) * (j - i))
#         return res


# Time Complexity- O(n) Space Complexity- O(1)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        low = 0
        high = len(height) - 1
        area = 0

        # till both pointers don't cross each other
        while low < high:
            # intial height
            ht = 0
            # width of the container
            width = high - low

            # when low pointer is less than high 
            if height[low] < height[high]:
                ht = height[low]
                # as we need taller line for more area, increase the low 
                low += 1
            else:
                ht = height[high]
                # as we need taller line for more area, decrease the high because that is less than low at this point
                high -= 1
            # find out the area with previously found and currently found
            area = max(area, ht * width)
        
        return area
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))