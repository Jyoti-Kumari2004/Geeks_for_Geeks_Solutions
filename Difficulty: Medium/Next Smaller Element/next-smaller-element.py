class Solution:
	def nextSmallerEle(self, arr):
		# code here
		st=[]
		res=[]
		for i in range(len(arr)-1,-1,-1):
		    if not st:
		        res.append(-1)
		    elif st[-1]<arr[i] and st:
		        res.append(st[-1])
		    else:
		        while st and st[-1]>=arr[i]:
		            st.pop()
		        if not st:
		            res.append(-1)
		        else:
		            res.append(st[-1])
		    st.append(arr[i])
	    return res[::-1]
		        