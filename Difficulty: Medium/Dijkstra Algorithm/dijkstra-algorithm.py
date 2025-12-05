import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        # for the first solution we are using priority queue:
        adjList=[[]for i in range(V)]
        for u,v,d in edges:
            adjList[u].append((v,d))
            adjList[v].append((u,d))
        
        pq = []                     # empty priority queue
        dist=[float('inf')]*V
        dist[src]=0
        heapq.heappush(pq, (0, src)) 
        while pq:
            d, node = heapq.heappop(pq) 
            if d != dist[node]:
                continue
            for u,dis in adjList[node]:
                if dist[u]>dis+dist[node]:
                    dist[u]=dis+dist[node]
                    heapq.heappush(pq,(dist[u],u))
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist
            
            