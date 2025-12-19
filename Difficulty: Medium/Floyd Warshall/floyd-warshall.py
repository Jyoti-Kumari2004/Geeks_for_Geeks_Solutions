class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != 100000000 and dist[via][j] != 100000000 :
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
        
        return dist
