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
            if node == None:
                return res
            res.append(node.val)
            for n in node.children:
                dfs(n,res)
            return res

        return dfs(root,[])
