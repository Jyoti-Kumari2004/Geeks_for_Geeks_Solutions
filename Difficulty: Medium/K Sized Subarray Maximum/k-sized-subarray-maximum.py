from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        i=0
        j=0
        li=deque()
        ans=[]
        while j<len(arr):
            while li and arr[j]>li[-1]:
                li.pop()
                
            li.append(arr[j])
            if j-i+1==k:
                if not li:
                    ans.append(0)
                else:
                    ans.append(li[0])
                if arr[i]==li[0]:
                    li.popleft()
                i+=1
            j+=1
        return ans
        