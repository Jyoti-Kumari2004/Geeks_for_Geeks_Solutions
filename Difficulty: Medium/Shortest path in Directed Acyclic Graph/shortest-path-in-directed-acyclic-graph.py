#User function Template for python3

from typing import List


class Solution:

    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        
        adjList=[[]for i in range(V)]
        for u,v,d in edges:
            adjList[u].append([v,d])
        # print(adjList)
        
        
        # toposort wala part
        stack=[]
        visited=[0]*V
        for i in range(V):
            if visited[i]==0:
                self.dfs(adjList,visited,stack,i)
        # print(stack)
        dist=[float('inf')]*V
        dist[0]=0
        while stack:
            node=stack.pop()
            #now relax the edge:
            for u,d in adjList[node]:
                if dist[u]>d+dist[node]:
                    dist[u]=d+dist[node]
        # print(dist)
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist
    def dfs(self, adjList,visited,stack,s):
        visited[s]=1
        for u,d in adjList[s]:
            if visited[u]==0:
                self.dfs(adjList,visited,stack,u)
        stack.append(s)
        return 
        
