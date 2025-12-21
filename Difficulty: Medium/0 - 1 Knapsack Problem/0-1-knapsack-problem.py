class Solution:
    def knapsack(self, W, val, wt):
        # code here
        n=len(wt)+1
        m=W+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    t[i][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if wt[i-1]<=j:
                    #have choice to pick or not pick
                    t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
                    
                else:
                    t[i][j]=t[i-1][j]
        return t[n-1][m-1]
