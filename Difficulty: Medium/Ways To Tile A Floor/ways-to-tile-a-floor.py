class Solution:
    def numberOfWays(self, n):
        # code here
        return self.solve(n)
    def solve(self,n):
        t=[None]*(n+1)
        t[0]=1
        t[1]=1
        for i in range(2,n+1):
            t[i]=t[i-1]+t[i-2]
        
        return t[n]
            
        