class Solution:
	def preGreaterEle(self, arr):
		# code here
		res=[]
		st=[]
		for i in range(len(arr)):
		    if not st:
		        res.append(-1)
		    elif st[-1]>arr[i] and st:
		        res.append(st[-1])
		    else:
		        while st and st[-1]<=arr[i]:
		            st.pop()
		        if not st:
		            res.append(-1)
		        else:
		            res.append(st[-1])
		    st.append(arr[i])
	    return res