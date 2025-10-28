class Solution:
    def findPages(self, arr, k):
        # code here
        n=len(arr)
        if k>n:
            return -1
            
        sum=0
        for i in range(n):
            sum+=arr[i]
        e=sum    
        s=max(arr)
        res=-1
        while s<=e:
            mid=s+(e-s)//2
            if self.isvalid(arr,n,k,mid)==True:
                res=mid
                e=mid-1
            else:
                s=mid+1
        return res
    def isvalid(self,arr,n,k,mid):
        stu=1
        sum=0
        for i in range(n):
            sum+=arr[i]
            if sum>mid:
                stu+=1
                sum=arr[i]
            if stu>k:
                return False
        return True
        
            
        

