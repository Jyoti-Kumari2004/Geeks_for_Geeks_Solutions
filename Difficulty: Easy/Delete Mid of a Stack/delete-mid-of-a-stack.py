import math
class Solution:
    def deleteMid(self, stack):
        #code here
        if len(stack)==0:
            return stack
        k=math.ceil((len(stack)+1)/2)
        self.solve(stack,k)
        return stack
    def solve(self,s,k):
        #base condition
        if k==1:
            s.pop()
            return 
        #store and pop
        temp=s.pop()
        #recurrsive function
        self.solve(s,k-1)
        #end mien push kar dena
        s.append(temp)
        #return the anssss
        return 
        
                