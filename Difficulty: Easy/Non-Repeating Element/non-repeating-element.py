#User function Template for python3

#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        h=defaultdict(int)
        for i in range(len(arr)):
            h[arr[i]]+=1
        for i in h:
            if h[i]==1:
                return i
        return 0
        
            

        
            
