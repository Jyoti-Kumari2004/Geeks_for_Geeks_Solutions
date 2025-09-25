'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    def lca(self,root, n1, n2):
        # Code here
        if root==None or root.data==n1 or root.data==n2:
            return root
        ls=self.lca(root.left,n1,n2)
        rs=self.lca(root.right,n1,n2)
        if ls and rs:
            return root
        elif ls and not rs:
            return ls
        else:
            return rs

