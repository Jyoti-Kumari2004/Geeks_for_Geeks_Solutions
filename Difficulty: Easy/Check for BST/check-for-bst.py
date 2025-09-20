'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def validity(root,minv=float('-inf'),maxv=float('inf')):
            if root==None:
                return True
            if root.data<minv or root.data>maxv:
                return False
            return validity(root.left,minv,root.data-1)and validity(root.right,root.data+1,maxv)
        return validity(root)
        
