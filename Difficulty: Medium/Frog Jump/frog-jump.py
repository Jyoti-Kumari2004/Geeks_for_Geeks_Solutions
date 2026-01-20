class Solution:
    def minCost(self, height):
        return self.solve(height,len(height)-1)
        # code here
    def solve(self,height,n):
        
        # if n==0:
        #     return 0
        # if n==1:
        #     return abs(height[1]-height[0])
        # l=abs(height[n]-height[n-1])+self.solve(height,n-1)
        # r=abs(height[n]-height[n-2])+self.solve(height,n-2)
        # return min(l,r)
        if len(height)==1:
            return 0
        if len(height)==2:
            return abs(height[1]-height[0])
        
        t=[0]*(len(height))
        t[1]=abs(height[1]-height[0])
        for i in range(2,len(height)):
            t[i]=min(t[i-1]+abs(height[i]-height[i-1]),t[i-2]+abs(height[i]-height[i-2]))
        return t[len(height)-1]