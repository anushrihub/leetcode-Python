# https://leetcode.com/problems/top-k-frequent-elements/description/
# Time Complexity- O(n log n) Space Complexity- O(n)

# class Solution:
#     def topKFrequent(self, nums: list[int], k: int):
#         count = {}
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         arr = []
#         for num, cnt in count.items():
#             # as we are going to sort the list we are keeping the count first because in pop we are deleting the elements from the last
#             arr.append([cnt, num])
#         arr.sort()

#         res = []
#         # we want k elements so till the result reaches k append the elements from arr
#         while len(res) < k:
#             # remove the pair and add the num in res
#             res.append(arr.pop()[1])
#         return res

# Time Complexity- O(n log k) Space Complexity- O(n + k)
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        map = {}
        # create a map
        for num in nums:
            map[num] = 1 + map.get(num, 0)

        heap = []
        # add into the heap, we want num with kth frequency hence count is added first because in mean heap
        for num, count in map.items():
            # as it's a min heap, heap will keep smallest 'count' on the top
            heapq.heappush(heap, (count, num))
            # when the heap is greater than k, pop it which will pop the low frequency num i.e. the value at root
            if len(heap) > k:
                heapq.heappop(heap)

        # create a result set
        result = []
        for i in range(k):
            # append the num in result which is at position 1
            result.append(heapq.heappop(heap)[1])
        return result


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 4], 2))
