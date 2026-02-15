# https://www.geeksforgeeks.org/problems/subset-sums2234/1

# Time Complexity - O(2 power n) Space Complexity - O(n)


class Solution:
    def subsetSums(self, arr):
        # code here
        # define the result set
        result = []

        # define the helper function
        def helper(index, sum):
            # base case
            if index >= len(arr):
                result.append(sum)
                return
            # call the function with next index and add the sum
            helper(index + 1, sum + arr[index])
            # call the function with next index
            helper(index + 1, sum)

        helper(0, 0)
        return result


s = Solution()
print(s.subsetSums([2, 3]))
