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

        res = collections.defaultdict(list)
        que = collections.deque([[root,0]])

        level = 0
        while que:
            node,l = que.popleft()
            res[l].append(node.val)
            if node.left:
                que.append([node.left,l+1])
            if node.right:
                que.append([node.right,l+1])

            level += 1

        ans = []
        for i in range(level):
            if res[i]:
                ans.append(res[i])

        return ans
