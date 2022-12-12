# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 == None: return root2
        if root2 == None: return root1

        stack = [[root1,root2]]

        while stack:
            t1,t2 = stack.pop()

            if t1 != None and t2 != None:
                t1.val += t2.val

                if t1.left == None:
                    t1.left = t2.left
                else:
                    stack.append([t1.left,t2.left])

                if t1.right == None:
                    t1.right = t2.right
                else:
                    stack.append([t1.right,t2.right])

        return root1