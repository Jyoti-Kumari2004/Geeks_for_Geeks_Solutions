class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        m=sum+1
        n=len(arr)+1
        t=[[None]*(sum+1) for i in range(len(arr)+1)]
        for i in range(n):
            for j in range(m):
                if i==0:
                    t[i][j]=False
                if j==0:
                    t[i][j]=True
        for i in range(1,n):
            for j in range(1,m):
                if arr[i-1]<=j:
                    t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[n-1][m-1]
        
        