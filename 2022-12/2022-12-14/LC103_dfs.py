# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []

        res = []
        def dfs(node,level):
            if level >= len(res):
                res.append(collections.deque([node.val]))
            else:
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)
            
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)

        dfs(root,0)
        return res