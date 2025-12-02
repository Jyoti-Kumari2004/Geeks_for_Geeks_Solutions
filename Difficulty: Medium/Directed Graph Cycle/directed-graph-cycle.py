class Solution:
    def isCyclic(self, V, edges):
        # code here
        adjList=[[]for i in range(V)]
        for u,v in edges:
            adjList[u].append(v)
        visited=[0]*V
        path=[0]*V
        for i in range(len(visited)):
            if visited[i]==0:
                if self.dfs(adjList,visited,path,i)==True:
                    return True
        return False
                
    
                
    def dfs(self,adjList,visited,path,s):
        visited[s]=1
        path[s]=1
        for u in adjList[s]:
            if visited[u]==0:
                if self.dfs(adjList,visited,path,u):
                    return True
            if visited[u]==1 and path[u]==1:
                return True
        path[s]=0
        return False
                