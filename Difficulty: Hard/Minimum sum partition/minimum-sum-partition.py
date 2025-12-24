#User function Template for python3
class Solution:
	def minDifference(self, arr):
		# code here
		lis=self.subsetSum(arr,sum(arr),len(arr))
        mini=float('inf')
        curr_diff=0
        N=sum(arr)
        r=sum(arr)//2

        if not lis:
            return 0
            
        for i in range(r+1):
            if lis[i]==True:
                curr_diff=abs(N-(2*i))
                mini=min(mini,curr_diff)
        return mini
    def subsetSum(self,nums,s,n):
        m=s+1
        n=n+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0:
                    t[i][j]=False
                if j==0:
                    t[i][j]=True
        for i in range(1,n):
            for j in range(1,m):
                if nums[i-1]<=j:
                    t[i][j]=t[i-1][j]or t[i-1][j-nums[i-1]]
                else:
                    t[i][j]=t[i-1][j]
        return t[n-1]
