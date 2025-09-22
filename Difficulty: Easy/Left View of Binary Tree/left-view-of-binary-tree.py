'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __init__(self):
        self.ans=[]
    def LeftView(self, root):
        # code here
        if root==None:
            return []
        q=deque()
        q.append(root)
        while len(q):
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.data)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            self.ans.append(level[0])
        return self.ans
            