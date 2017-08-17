# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            return q == None
        elif q is None:
            return False
        if q.val == p.val:
            return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        else:
            return False