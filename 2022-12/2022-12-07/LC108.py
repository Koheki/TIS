# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def bst(arr):
            if len(arr) == 0:
                return
            n = len(arr)//2
            node = TreeNode(arr[n])
            node.left = bst(arr[:n])
            node.right = bst(arr[n+1:])
            return node

        return bst(nums)