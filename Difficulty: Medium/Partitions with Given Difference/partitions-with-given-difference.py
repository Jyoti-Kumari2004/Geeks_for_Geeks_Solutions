class Solution:
    def countPartitions(self, arr, diff):
        # code here
        s1=(diff+sum(arr))//2
        if (diff+sum(arr))%2!=0:
            return 0
        if diff>sum(arr):
            return 0
        return self.countSubsetsum(arr,s1,len(arr))
    def countSubsetsum(self,arr,s,n):
        count=0
		ch=[]
		for i in arr:
		    if i==0:
		        count+=1
		    else:
		        ch.append(i)
		
		m=s+1
		n=len(ch)+1
		t=[[None]*m for i in range(n)]
		for i in range(n):
		    for j in range(m):
		        if i==0:
		            t[i][j]=0
		        if j==0:
		            t[i][j]=1
		for i in range(1,n):
		    for j in range(1,m):
		        if ch[i-1]<=j:
		            t[i][j]=t[i-1][j]+t[i-1][j-ch[i-1]]
		        else:
		            t[i][j]=t[i-1][j]
		if count>0:
		    return t[n-1][m-1]*(2**count)
		
	    return t[n-1][m-1]
                    
        
