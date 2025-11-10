from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		visited=[False]*V
		adj=[[]for i in range(V)]
		for u,v in edges:
		    self.addEdge(u,v,adj)
		for i in range(len(adj)):
		    if visited[i]==False:
		        if self.bfs(adj,i,visited):
		            return True
		return False
		
    def bfs(self,adj,s,visited):
        
        q=deque()
        q.append((s,-1))
        visited[s]=True
        while q:
            s,p=q.popleft()
            for i in adj[s]:
                if visited[i]==False:
                    q.append((i,s))
                    visited[i]=True
                elif p!=i:
                    return True
        return False
            

    
            
		
		
		
		
		
	def addEdge(self,u,v,adj):
	    adj[u].append(v)
	    adj[v].append(u)
	    
	    
	    