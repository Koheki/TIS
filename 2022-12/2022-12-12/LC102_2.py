# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []

        res = []
        que = collections.deque([root])

        depth = 0
        while que:
            size = len(que)
            res.append([])

            for i in range(size):
                node = que.popleft()
                res[depth].append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            depth += 1

        return res