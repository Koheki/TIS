"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node != None:
                res.append(node.val)

                tmp = []
                for n in node.children:
                    tmp.append(n)

                while tmp:
                    stack.append(tmp.pop())

        return res