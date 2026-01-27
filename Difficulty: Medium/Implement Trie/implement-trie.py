#User function Template for python3
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
        

class Trie:
    def __init__(self):
        # implement Trie
        self.root=TrieNode()
        
    def insert(self, word: str):
       # insert word into Trie
        node=self.root
        for ch in word:
            if not node.containskey(ch):
               node.put(ch,TrieNode())
            node=node.get(ch)
        node.setEnd()

    def search(self, word: str) -> bool:
        # search word in the Trie
        node=self.root
        for ch in word:
            if not node.containskey(ch):
                return False
            node=node.get(ch)
        # if node.isEnd==True:
        #     return True
        # else:
        #     return False or you can simply return node.isEnd value
        return node.isEnd()
         
         

    def isPrefix(self, word: str) -> bool:
        
         # search prefix word in the Trie
        node=self.root
        for ch in word:
            if not node.containskey(ch):
                return False
            node=node.get(ch)
        return True
        
                
         
         
         
         
         
         
         