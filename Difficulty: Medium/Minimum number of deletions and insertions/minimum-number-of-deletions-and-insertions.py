#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		# code here
		n=len(s1)+1
		m=len(s2)+1
		t=[[None]*m for i in range(n)]
		for i in range(n):
		    for j in range(m):
		        if i==0 or j==0:
		            t[i][j]=0
	    for i in range(1,n):
	        for j in range(1,m):
	            if s1[i-1]==s2[j-1]:
	                t[i][j]=1+t[i-1][j-1]
	            else:
	                t[i][j]=max(t[i-1][j],t[i][j-1])
	    return len(s1)-t[n-1][m-1]+len(s2)-t[n-1][m-1]