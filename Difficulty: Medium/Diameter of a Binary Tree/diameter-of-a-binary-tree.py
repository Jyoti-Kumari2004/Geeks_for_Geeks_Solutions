'''
# Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def __init__(self):
        self.res=float('-inf')
    def diameter(self, root):
        # code here
        self.solve(root)
        return self.res-1
        
        
    def solve(self,root):
        if root==None:
            return 0
        l=self.solve(root.left)
        r=self.solve(root.right)
        temp=max(l,r)+1
        ans=max(temp,l+r+1)
        self.res=max(self.res,ans)
        return temp
        
        