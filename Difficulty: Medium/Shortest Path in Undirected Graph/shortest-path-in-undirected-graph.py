class Solution:
    def shortestPath(self, V, edges, src):
        # code here
        #edges to adjList:
        adjList=[[]for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        dist=[float('inf')]*V
        
        q=deque()
        dist[src]=0
        q.append((src,0))
        while q:
            node,dis=q.popleft()
            for u in adjList[node]:
                if (dist[u]>dis+1):
                    dist[u]=dis+1
                    q.append((u,dist[u]))
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist
                        
                
                    
                    
                    
        
        
