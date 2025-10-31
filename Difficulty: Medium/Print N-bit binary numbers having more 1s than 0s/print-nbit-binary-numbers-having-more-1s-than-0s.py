#User function Template for python3
class Solution:
	def NBitBinary(self, n):
		# code here
		ans=[]
		one=0
		z=0
		op=""
		self.solve(op,n,one,z,ans)
		return ans
	    
	def solve(self,op,n,one,z,ans):
	    if n==0:
	        ans.append(op)
	        return
	    op1=op
	    op1+="1"
	    self.solve(op1,n-1,one+1,z,ans)
	    if one>z:
	        op2=op
	        op2+="0"
	        self.solve(op2,n-1,one,z+1,ans)
