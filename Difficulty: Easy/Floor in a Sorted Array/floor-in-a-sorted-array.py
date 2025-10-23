class Solution:
    def findFloor(self, arr, x):
        # code here
        s=0
        e=len(arr)-1
        mid=0
        ans=-1
        while s<=e:
            mid=s+(e-s)//2
            if arr[mid]<=x:
                ans=mid
                s=mid+1
            else:
                e=mid-1
        return ans
        