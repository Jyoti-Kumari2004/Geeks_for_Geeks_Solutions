class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        i=0
        j=0
        summ=0
        maxx=0
        while j<len(arr):
            summ+=arr[j]
            if j-i+1==k:
                maxx=max(summ,maxx)
                summ-=arr[i]
                i+=1
            j+=1
        return maxx
                