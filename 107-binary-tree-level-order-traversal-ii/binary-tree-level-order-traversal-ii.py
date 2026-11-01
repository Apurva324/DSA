# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []

        queue = deque()
        queue.append(root)

        res = []

        while queue:
            level_size = len(queue)
            temp = []

            while (level_size != 0):
                node = queue.popleft()
                temp.append(node.val)

                if (node.left != None):
                    queue.append(node.left)

                if (node.right != None):
                    queue.append(node.right)

                level_size -= 1

            res.append(temp)
        return res[::-1]
        