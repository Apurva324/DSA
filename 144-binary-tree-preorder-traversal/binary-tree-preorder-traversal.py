# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def func(node):
            if node == None:
                return
            result.append(node.val)
            func(node.left)
            func(node.right)

        func(root)

        return result
        