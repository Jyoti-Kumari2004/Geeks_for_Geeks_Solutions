class Solution:
    def twoRepeated(self, arr):
        # code here
        # one solution is 
        # ans=[]
        # h=[0]*(len(arr)-1)
        # for i in range(len(arr)):
        #     h[arr[i]]+=1
        # for i in range(len(h)):
        #     if h[i]>1:
        #         ans.append(i)
        # return ans
        
        #optimum could be use -ve sign..when visited mark them -ve and move..if you revisit 
        #..and it marked -ve then you got your repeating element
        ans=[]
        for i in range(len(arr)):
            idx=abs(arr[i])-1
            if arr[idx]<0:
                ans.append(abs(arr[i]))
            else:
                arr[idx]=-arr[idx]
            
            
        return ans
            
            
            
