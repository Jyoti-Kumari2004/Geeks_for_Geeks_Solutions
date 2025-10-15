class Solution:
    def reverseStack(self, st):
        # code here
        #using another stack,but not good as we aure using extra space
        # s=[]
        # for i in range(len(st)-1,-1,-1):
        #     s.append(st[i])
        # print(s)
        
        #now we will use recurssion to solve this
        if len(st)==1:
            return 
        temp=st.pop()
        self.reverseStack(st)
        self.insert(st,temp)
        return 
    def insert(self,s,ele):
        if len(s)==0:
            s.append(ele)
            return 
        temp=s.pop()
        self.insert(s,ele)
        s.append(temp)
        return
