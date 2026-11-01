# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        ans = None
        def func(node, val):
            nonlocal ans

            if node == None:
                return 

            if node.val == val:
                ans = node
                return 
            if node.val > val:
                func(node.left, val)
            else:
                func(node.right, val)
        func(root, val)
        return ans
        