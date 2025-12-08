#User function Template for python3
import heapq
from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if end>=100000:
            return -1
        if start==end:
            return 0
        dist=[float('inf')]*100000
        pq=[]
        heapq.heappush(pq,(0,start))
        while pq:
            steps,num=heapq.heappop(pq)
            if end==num:
                    return dist[num]
            for i in arr:
                nx_num=(num*i)%100000
                if dist[nx_num]>steps+1:
                    dist[nx_num]=steps+1
                    heapq.heappush(pq,(steps+1,nx_num))
                
        return -1
                
                
                