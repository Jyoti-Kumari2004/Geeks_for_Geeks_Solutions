class Solution:
    def catchThieves(self, arr, k):
        i=0
        j=0
        n=len(arr)
        count=0
        while i<len(arr) and j<len(arr):
            while i<n and arr[i]!="P":
                i+=1
                
            while j<n and arr[j]!="T":
                j+=1
            if i==n or j==n:
                return count
            if abs(i-j)<=k:
                count+=1
                i+=1
                j+=1
            elif i<j:
                i+=1
            else:
                j+=1
        return count
           
