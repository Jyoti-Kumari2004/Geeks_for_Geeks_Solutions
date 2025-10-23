#User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        # code here
        s=0
        e=len(arr)-1
        mid=0
        while s<=e:
            mid=s+(e-s)//2
            if arr[mid]==target:
                return mid
            if mid<len(arr)-1 and arr[mid+1]==target:
                return mid+1
            if mid>0 and arr[mid-1]==target:
                return mid-1
            elif arr[mid]<target:
                s=mid+1
            else:
                e=mid-1
        return -1