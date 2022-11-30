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
        
        levels = []
        level = 0
        que = collections.deque([[root]])

        while que:
            levels.append([])
            lenght = len(que)

            for i in range(lenght):
                node = que.popleft()
                levels[level].append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            level += 1

        return levels

