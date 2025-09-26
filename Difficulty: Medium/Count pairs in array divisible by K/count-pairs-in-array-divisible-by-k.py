#User function Template for python3
from collections import defaultdict
class Solution:
    def countKdivPairs(self, arr, n, k):
        #code here
        ans=0
        mod=0
        h=defaultdict(int)
        for i in range(len(arr)):
            mod=arr[i]%k
            x=k-mod
            if mod!=0:
                ans+=h[x]
            else:
                ans+=h[0]
            h[mod]+=1
        return ans
        
            
            
