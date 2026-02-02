class Solution:
    def getMaxArea(self, arr):
        # code here
        ns=self.nextSmaller(arr)
        ps=self.prevSmaller(arr)
        area=0
        
        for i in range(len(arr)):
            height=arr[i]
            width=ns[i]-ps[i]-1
            area=max(area,height*width)
        return area
            
    def nextSmaller(self,arr):
        st=[]
        res=[]
        for i  in range(len(arr)-1,-1,-1):
            if not st:
                res.append(len(arr))
            elif arr[st[-1]]<arr[i]:
                res.append(st[-1])
            else:
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if not st:
                    res.append(len(arr))
                else:
                    res.append(st[-1])
            st.append(i)
        return res[::-1]
    def prevSmaller(self,arr):
        st=[]
        res=[]
        for i  in range(len(arr)):
            if not st:
                res.append(-1)
            elif arr[st[-1]]<arr[i]:
                res.append(st[-1])
            else:
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if not st:
                    res.append(-1)
                else:
                    res.append(st[-1])
            st.append(i)
        return res
        
        