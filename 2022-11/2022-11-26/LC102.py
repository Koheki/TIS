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
        que = collections.deque([[root]])

        while que:
            node = que.popleft()

            l,r = [],[]
            for n in node:
                if n != None:
                    l.append(n.left)
                    l.append(n.right)
                    r.append(n.val)

            if len(l) > 0 and len(r) > 0:
                que.append(l)
                res.append(r)

        return res

