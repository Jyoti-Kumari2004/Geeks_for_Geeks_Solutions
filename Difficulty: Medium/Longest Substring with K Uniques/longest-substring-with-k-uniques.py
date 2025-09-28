from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        m=-1
        h=defaultdict(int)
        j=0
        i=0
        while j<len(s):
            h[s[j]]+=1
            
            if len(h)==k:
                m=max(m,j-i+1)
            elif len(h)>k:
                while len(h)>k:
                    
                    h[s[i]]-=1
                    if h[s[i]]==0:
                        h.pop(s[i])
                    i+=1
            j+=1
        return m
                
        