# https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        # need something from which I can start linking the lsit
        prenode = ListNode(-1)
        
        # This is the changing part
        prev = prenode
        # below condition is same as l1 and l2 not none
        while l1 and l2:
            # we are checking the values
            if l1.val <= l2.val:
                # and we are connecting the entire node
                prev.next = l1
                # we need to move forward so updating the list1 pointer
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        # this if condition says if l1 has value
        if l1:
            prev.next = l1
        # this if condition says if l2 has value  
        elif l2:
            prev.next = l2

        return prenode.next


            