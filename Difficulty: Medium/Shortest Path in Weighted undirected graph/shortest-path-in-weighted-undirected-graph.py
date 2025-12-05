#User function Template for python3
import heapq
from typing import List
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        if not edges:
            return -1
        V=n
        adjList=[[]for i in range(V)]
        for u,v,d in edges:
            u-=1
            v-=1
            adjList[u].append((v,d))
            adjList[v].append((u,d))
        
        
        pq = []
        parent=[-1]*V
        dist=[float('inf')]*V
        dist[0]=0
        heapq.heappush(pq, (0, 0)) 
        while pq:
            d, node = heapq.heappop(pq) 
            if d != dist[node]:
                continue
            for u,dis in adjList[node]:
                if dist[u]>dis+dist[node]:
                    dist[u]=dis+dist[node]
                    heapq.heappush(pq,(dist[u],u))
                    parent[u]=node
        if dist[-1]==float('inf'):
            return [-1]
        
        
        path=[]
        curr=n-1
        while curr!=-1:
            path.append(curr+1)
            curr=parent[curr]
        return [dist[-1]]+path
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return dist
        