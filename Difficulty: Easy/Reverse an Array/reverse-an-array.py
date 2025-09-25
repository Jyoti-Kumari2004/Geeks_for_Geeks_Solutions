class Solution:
    def reverseArray(self, arr):
        # code here
        #1.
        # return arr.reverse()
        #2.
        #return arr[::-1]
        #3.
        # j=len(arr)-1
        # i=0
        # while i<j:
        #     arr[i],arr[j]=arr[j],arr[i]
        #     i+=1
        #     j-=1
        # return arr
        n=len(arr)-1
        for i in range(len(arr)//2):
            arr[i],arr[n-i]=arr[n-i],arr[i]
        return arr
            
        
        
        