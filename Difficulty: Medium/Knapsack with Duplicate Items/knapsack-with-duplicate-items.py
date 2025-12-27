class Solution:
    def knapSack(self, val, wt, capacity):
        # code here
        m=capacity+1
        n=len(wt)+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0:
                    t[i][j]=0
                if j==0:
                    t[i][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if wt[i-1]<=j:
                    t[i][j]=max(val[i-1]+t[i][j-wt[i-1]],t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        return t[n-1][m-1]