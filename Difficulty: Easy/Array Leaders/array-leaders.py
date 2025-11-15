class Solution:
    def leaders(self, arr):
        # code here
        res=[]
        n=len(arr)
        max=0
        for i in range(n-1,-1,-1):
            if arr[i]>=max:
                res.append(arr[i])
                max=arr[i]
        return res[::-1]
            
            
            
            