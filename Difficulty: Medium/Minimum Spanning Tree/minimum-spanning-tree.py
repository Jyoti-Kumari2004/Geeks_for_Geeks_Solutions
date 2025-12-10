import heapq
class Solution:
    def spanningTree(self, V, edges):
        # code here
        adjList=[[]for i in range(V)]
        for u,v,w in edges:
            adjList[u].append((v,w))
            adjList[v].append((u,w))
        mst=[]
        visited=[False]*V
        sum=0
        pq=[]
        heapq.heappush(pq,(0,0,-1))
        while pq:
            wt,node,parent=heapq.heappop(pq)
            if visited[node]==True:
                continue
            visited[node]=True
            
            sum+=wt
            if parent!=-1:
                mst.append((parent,node))
            for u,w in adjList[node]:
                if visited[u]==False:
                    heapq.heappush(pq,(w,u,node))
                
        
        return sum
                