# https://leetcode.com/problems/linked-list-cycle/
# time complexity- O(n) Space Complexity- O(1)

# Definition for singly-linked list.
# using set
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head):
#         seen = set()
#         curr = head
#         while curr is not None:
#             if curr in seen:
#                 return True
#             seen.add(curr)
#             curr = curr.next
#         return False
    

# using Floyd's Cycle Finding Algorithm
# time complexity- O(n) space complexity- O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):

        slow = fast = head

        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

