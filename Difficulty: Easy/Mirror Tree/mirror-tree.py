'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque
class Solution:
    
    def mirror(self, root):
        # # # Code here
        
        #using dfs traversal and using recurssion also
        # if root==None:
        #     return None
        # root.right,root.left=root.left,root.right
        # self.mirror(root.left)
        # self.mirror(root.right)
        # return root
        
        
        
        #using bfs traversal
        
        if root==None:
            return []
        q=deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node=q.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                

        return root
                
        