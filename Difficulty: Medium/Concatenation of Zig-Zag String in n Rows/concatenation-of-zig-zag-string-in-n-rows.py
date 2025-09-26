#User function Template for python3

class Solution:

    def convert(self, Str, n):
        # code here
        if n==1:
            return Str
        ans=[""]*n
        curr_row=0
        for ch in Str:
            ans[curr_row]+=ch
            if curr_row==0:
                op=1
            if curr_row==n-1:
                op=-1
            curr_row+=op
        return "".join(ans)
        
            
                
            
            
            