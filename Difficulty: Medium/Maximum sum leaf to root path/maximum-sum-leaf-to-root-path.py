#User function Template for python3
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''
class Solution:
    def maxPathSum(self, root):
        # code here
        return self.solve(root)
        
    def solve(self,root):
        if root==None:
            return 0
        l=self.solve(root.left)
        r=self.solve(root.right)
        if not l and not r:
            return root.data
        if l and not r:
            return root.data+l
        elif r and not l:
            return root.data+r
        else:
            return max(l,r)+root.data