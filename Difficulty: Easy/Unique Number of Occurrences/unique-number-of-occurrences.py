
from typing import List
from collections import defaultdict

class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        # code here
        h=defaultdict(int)
        for i in range(len(arr)):
            h[arr[i]]+=1
        li=set(freq for freq in h.values())
        return (len(li)==len(h))
            
        

