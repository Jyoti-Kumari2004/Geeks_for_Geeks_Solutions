class Solution:
	def nearest(self, grid):
		# code here
		n=len(grid)
		m=len(grid[0])
		visited=[[False]*m for i in range(n)]
		mat=[[0]*m for i in range(n)]
		q=deque()
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==1:
		            q.append((i,j,0))
		            mat[i][j]=0
		            visited[i][j]=True
		            
		
		dir=[[0,-1],[0,1],[1,0],[-1,0]]
		while q:
		    i,j,s=q.popleft()
		    mat[i][j]=s
		    for x,y in dir:
		        if 0<=x+i<n and 0<=y+j<m:
		            if visited[x+i][y+j]==False:
		                q.append((x+i,j+y,s+1))
		                visited[x+i][y+j]=True
		return mat
		                
		                
		