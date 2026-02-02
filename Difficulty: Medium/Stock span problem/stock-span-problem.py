class Solution:
    def calculateSpan(self, arr):
        # code here
        res=[]
        st=[]
        for i in range(len(arr)):
            if not st:
                res.append(i+1)
            elif arr[st[-1]]>arr[i]:
                res.append(i-st[-1])
            else:
                while st and arr[st[-1]]<=arr[i]:
                    st.pop()
                if not st:
                    res.append(i+1)
                else:
                    res.append(i-st[-1])
            st.append(i)
        return res
        
        