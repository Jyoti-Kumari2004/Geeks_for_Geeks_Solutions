from collections import defaultdict
class Solution:
    def findOrder(self, words):
        # code here
        
        d=defaultdict(int)
        alpha="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alpha)):
            d[alpha[i]]=i
        # maping ho gyi
        indegree=[0]*26
        i=0
        j=1
        adjList=[[]for i in range(26)]
        while j<len(words):
            w1=words[i]
            w2=words[j]
            if len(w1)>len(w2) and w1.startswith(w2):
                return ""
                
            x=0
            y=0
            while x<len(w1) and y<len(w2):
                if w1[x]!=w2[y]:
                    pos1=d[w1[x]]
                    pos2=d[w2[y]]
                    adjList[pos1].append(pos2)
                    indegree[pos2]+=1
                    break
                x+=1
                y+=1
            i+=1
            j+=1
       
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
        used = set()
        for w in words:
            for ch in w:
                used.add(d[ch])
        order=""
        for i in res:
            if i in used:
                order+=alpha[i]
        if len(used)!=len(order):
            return ""
        # print(order,used)
        else:
            return order
            
                        
            
        
        