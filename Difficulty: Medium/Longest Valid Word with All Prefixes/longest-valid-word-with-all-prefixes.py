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
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for ch in word:
            if not node.containskey(ch):
                node.put(ch,TrieNode())
            node=node.get(ch)
        node.setEnd()
    def checkAllPrefExists(self,word):
        node=self.root
        for ch in word:
            if node.containskey(ch):
                node=node.get(ch)
                if node.isEnd()==False:
                    return False
            else:
                return False
        return True
                
            
    def longestValidWord(self, words):
        # code here 
        trie=Solution()
        for word in words:
            trie.insert(word)
        lg=""
        for word in words:
            if trie.checkAllPrefExists(word):
                if len(word)>len(lg):
                    lg=word
                elif len(word)==len(lg) and word<lg:
                    lg=word
                    
        if lg=="":
            return ""

        return lg
        
        
        
        
        
        
        
        
        