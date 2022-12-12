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

        que = collections.deque([[root,1]])

        while que:
            node,n = que.popleft()
            if node != None:
                if node.left == None and node.right == None:
                    return n
                que.append([node.left,n+1])
                que.append([node.right,n+1])