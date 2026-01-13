class Solution:
    def canServe(self, arr):
        # code here 
        change=0
        money=0
        five=0
        ten=0
        for i in range(len(arr)):
            if arr[i]==5:
                five+=1
            if arr[i]==10 :
                ten+=1
                if five>=1:
                    five-=1
                else:
                    return False
            if arr[i]==20 :
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                
                else:
                    return False

        return True
                
                
            
            
            
        