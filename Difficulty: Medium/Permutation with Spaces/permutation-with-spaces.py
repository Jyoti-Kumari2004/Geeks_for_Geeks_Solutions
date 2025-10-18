#User function Template for python3


class Solution:

    def permutation(self, s):
        ans=[]
        ip=s
        op=""
        op+=ip[0]
        ip=ip[1:]
        self.solve(ip,op,ans)
        return ans
    def solve(self,ip,op,ans):
        if len(ip)==0:
            ans.append(op)
            return 
        op1=op
        op2=op
        op1+=" "+ip[0]
        op2+=ip[0]
        ip=ip[1:]
        self.solve(ip,op1,ans)
        self.solve(ip,op2,ans)

