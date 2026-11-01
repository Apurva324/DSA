# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def func(left,right):
            if ( left == None and right == None):
                return True
            if (left == None or right == None):
                return False
            if (left.val != right.val):
                return False

            r1 = func(left.left, right.right)
            r2 = func(left.right, right.left)

            if r1 == True and r2 == True:
                return True
            return False

        return func(root.left,root.right)