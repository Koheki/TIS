# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1

        mindepth = float("INF")
        if root.left != None:
            mindepth = min(self.minDepth(root.left),mindepth)
        if root.right != None:
            mindepth = min(self.minDepth(root.right),mindepth)

        return mindepth+1