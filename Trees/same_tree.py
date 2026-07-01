# https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p:TreeNode, q:TreeNode):
        # base case
        if p is None and q is None:
            return True
        # check if any of the tree is none 
        if p is None or q is None:
            return False
        # check the value for both trees are equal
        if p.val != q.val:
            return False
        # recurse the tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

if __name__ == "__main__":
    # Build tree 1:    1
    #                 / \
    #                2   3
    p = TreeNode(1, TreeNode(2), TreeNode(3))

    # Build tree 2:    1
    #                 / \
    #                2   3
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    sol = Solution()
    result = sol.isSameTree(p, q)
    print("Are trees the same?", result)