#User function Template for python3

class Solution:
    def firstIndex(self, arr):
    # Your code goes here
        s=0
        e=len(arr)-1
        mid=0
        ans=-1
        while s<=e:
            mid=s+(e-s)//2
            if arr[mid]==1:
                ans=mid
                e=mid-1
            else:
                s=mid+1
                
        return ans
        

