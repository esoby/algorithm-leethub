# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def maxDepth(node):
            nonlocal diameter

            if not node:
                return 0

            ld = maxDepth(node.left)
            rd = maxDepth(node.right)
            diameter = max(diameter, ld + rd)

            return max(ld, rd) + 1
        
        maxDepth(root)
        return diameter