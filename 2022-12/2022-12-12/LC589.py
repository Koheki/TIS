"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if root == None:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            tmp = []
            for v in node.children:
                if v:
                    tmp.append(v)
            stack.extend(tmp[::-1])
        return res
