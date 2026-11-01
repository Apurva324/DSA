# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def func(node,p,q):
            nonlocal ans

            if node == None:
                return 0

            left = func(node.left,p,q)
            right = func(node.right,p,q)

            own = 0
            if node == p or node == q:
                own = 1

            total = left + right + own

            if total == 2 and ans == None:
                ans = node

            return total

        func(root,p,q)
        return ans

        