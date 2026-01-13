#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, s):
		# Code here
		n=len(s)+1
        m=len(s)+1
        str1=s
        str2=s
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    t[i][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if str1[i-1]==str2[j-1] and i!=j:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[n-1][m-1]