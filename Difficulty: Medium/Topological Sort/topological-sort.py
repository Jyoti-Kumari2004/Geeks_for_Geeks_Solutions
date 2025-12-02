from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # this is by using bfs
        adjList=[[]for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
        indegree=[0]*V
        for i in range(len(adjList)):
            for j in adjList[i]:
               indegree[j]+=1
        res=[]
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            res.append(node)
            for u in adjList[node]:
                indegree[u]-=1
                if indegree[u]==0:
                    q.append(u)
            
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     # Code here
    
            
    # this was  using the dfs traversal
    #     visited=[0]*V
    #     stack=[]
        # adjList=[[]for _ in range(V)]
        # for u,v in edges:
        #     adjList[u].append(v)
    #     for j in range(V):
    #         if visited[j]==0:
    #             self.dfs(adjList,visited,stack,j)
    #     return stack[::-1]
    # def dfs(self,adjList,visited,stack,s):
    #     visited[s]=1
    #     for u in adjList[s]:
    #         if visited[u]==0:
    #             self.dfs(adjList,visited,stack,u)
    #     stack.append(s)
    #     return
    
    
    
          
        
        