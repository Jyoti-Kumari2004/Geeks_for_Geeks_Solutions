class Solution:
    def findKRotation(self, arr):
        # code here
        #if sorted hai to we will use binary serachi in any sitiuation
        s=0 
        e=len(arr)-1
        mid=0
        ans=0
        while s<=e:
            mid=s+(e-s)//2
            if arr[mid]<=arr[0] and arr[mid]<=arr[-1]:
                ans=mid
                e=mid-1
            else:
                s=mid+1
            
            
        return ans
        