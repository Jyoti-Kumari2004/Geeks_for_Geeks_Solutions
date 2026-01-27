#one way, but it will take more time

# class TrieNode:
#     def __init__(self):
#         self.links=[None]*26
#         self.flag=False
#     def containskey(self,ch):
#         return self.links[ord(ch)-ord('a')] is not None
#     def get(self,ch):
#         return self.links[ord(ch)-ord('a')]
#     def put(self,ch,node):
#         self.links[ord(ch)-ord('a')]=node
#         return 
#     def setEnd(self):
#         self.flag=True
#     def isEnd(self):
#         return self.flag


# class Solution:
#     def __init__(self):
#         self.root=TrieNode()
#     def insert(self,word):
#         node=self.root
#         for ch in word:
#             if not node.containskey(ch):
#                 node.put(ch,TrieNode())
#             node=node.get(ch)
#         node.setEnd()
#     def checkAllPrefExists(self,word):
#         node=self.root
#         for ch in word:
#             if node.containskey(ch):
#                 node=node.get(ch)
#                 if node.isEnd()==False:
#                     return False
#             else:
#                 return False
#         return True
                
#     def countSubs(self, s):
#         # code here
#         count=0
#         trie=Solution()
#         for i in range(len(s)):
#             st=""
#             for j in range(i,len(s)):
#                 st=st+s[j]
#                 if not trie.checkAllPrefExists(st):
#                     count+=1
#                     trie.insert(st)
                    
#         return count
                
                
class TrieNode:
    def __init__(self):
        self.links=[None]*26
        self.flag=False
    def containskey(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    def put(self,ch,node):
        self.links[ord(ch)-ord('a')]=node
        return 
    def setEnd(self):
        self.flag=True
    def isEnd(self):
        return self.flag


class Solution:
    
    def countSubs(self, s):
        # code here
        root=TrieNode()
        count=0
        for i in range(len(s)):
            node=root
            for j in range(i,len(s)):
                if not node.containskey(s[j]):
                    count+=1
                    node.put(s[j],TrieNode())
                node=node.get(s[j])
                    
        return count
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        