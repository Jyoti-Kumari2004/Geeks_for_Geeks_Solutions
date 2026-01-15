class Solution:
    def __init__(self):
        self.t=[[-1]*101 for i in range(101)]
    def matrixMultiplication(self, arr):
        # code here
        return (self.bottom_up(arr,1,len(arr)-1))
    def bottom_up(self,arr,i,j):
        if i>=j:
            return 0
        if self.t[i][j]!=-1:
            return self.t[i][j]
        mn=float('inf')
        for k in range(i,j):
            temp_ans=self.bottom_up(arr,i,k)+self.bottom_up(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
            if temp_ans<mn:
                mn=temp_ans
        self.t[i][j]=mn
        return self.t[i][j]
        
    #this is recursive solution ....time limit exceede so we will do memoization to reduce time complexity
    # def solve(self,arr,i,j):
        # if i>=j:
        #     return 0
        # mn=float('inf')
        # for k in range(i,j):
        #     temp_ans=self.solve(arr,i,k)+self.solve(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        #     if temp_ans<mn:
        #         mn=temp_ans
        # return mn