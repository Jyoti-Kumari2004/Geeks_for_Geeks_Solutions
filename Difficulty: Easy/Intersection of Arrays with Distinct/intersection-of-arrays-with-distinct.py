class Solution:
    def intersectSize(self,a, b):
        # code here
        i=0
        j=0
        count=0
        a.sort()
        b.sort()
       
        while i<len(a) and j<len(b):
            if i>0 and a[i]==a[i-1]:
                i+=1
            if j>0 and b[j]==b[j-1]:
                j+=1
            if a[i]==b[j]:
                count+=1
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            else:
                j+=1
        return count
            
            
