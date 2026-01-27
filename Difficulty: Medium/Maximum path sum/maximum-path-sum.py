'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __init__(self):
        self.res=float('-inf')
    
    def findMaxSum(self, root): 
        # code here
        self.solve(root,self.res)
        return self.res
        
        
        
    def solve(self,root,res):
        if root==None:
            return 0
        l=self.solve(root.left,self.res)
        r=self.solve(root.right,self.res)
        temp=max(max(l,r)+root.data,root.data)
        ans=max(temp,l+r+root.data)
        self.res=max(ans,self.res)
        return temp