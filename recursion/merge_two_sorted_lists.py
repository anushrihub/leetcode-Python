# https://leetcode.com/problems/merge-two-sorted-lists/
# Time Complexity- O() Space Complexity- O()

# recursion

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            # if the l1 value is less than l2 value
            if l1.val <= l2.val:
                # attach the next to list1 object
                prev.next = l1
                # update the node
                l1 = l1.next
            else:
                # attach the next to list2 object
                prev.next = l2
                # update the node
                l2 = l2.next
            # update the prev to next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        if l1:
            prev.next = l1
        else:
            prev.next = l2

        return prehead.next

