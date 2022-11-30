"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def dfs(node,res):
            if root == None:
                return res
            else:
                res.append(node.val)
                for n in node.children:
                    dfs(n,res)
            return res

        res = dfs(root,[])

        return res