# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def maxVal(node):
            if node == None:
                return float("-INF")
            v = node.val
            leftMax = maxVal(node.left)
            rightMax = maxVal(node.right)
            return max(v,max(leftMax,rightMax))

        def minVal(node):
            if node == None:
                return float("INF")
            v = node.val
            leftMin = minVal(node.left)
            rightMin = minVal(node.right)
            return min(v,min(leftMin,rightMin))

        def isBST(node):
            if node == None:
                return True
            if node.left != None and maxVal(node.left) >= node.val:
                return False
            if node.right != None and minVal(node.right) <= node.val:
                return False

            subleft = isBST(node.left)
            subright = isBST(node.right)

            if subleft and subright:
                return True
            else:
                return False

        return isBST(root)


