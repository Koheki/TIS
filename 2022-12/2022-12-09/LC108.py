# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def bst(nums,left,right):
            if left > right:
                return None
            mid = left + (right-left)//2
            tree = TreeNode(nums[mid])
            tree.left = bst(nums,left,mid-1)
            tree.right = bst(nums,mid+1,right)

            return tree
        
        return bst(nums,0,len(nums)-1)
