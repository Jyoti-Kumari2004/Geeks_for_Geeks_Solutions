#User function Template for python3
from collections import deque
class Solution:
    def firstNegInt(self, arr, k): 
         # code here 
        i=0
        j=0
        n=[]
        ans=[]
        while j<len(arr):
            if arr[j]<0:
                n.append(arr[j])
            if j-i+1<k:
                 j+=1
            elif j-i+1==k:
                #calculations +slide the window
                if len(n)==0:
                    ans.append(0)
                else:
                    #compare with the first elemnt
                    ans.append(n[0])
                    if arr[i]==n[0]:
                        n.pop(0)
                i+=1
                j+=1
        return ans
            
