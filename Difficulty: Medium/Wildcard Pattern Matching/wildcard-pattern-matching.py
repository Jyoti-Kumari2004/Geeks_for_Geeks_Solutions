class Solution:
    def wildCard(self, txt, pat):
        # code here
        n=len(txt)+1
        m=len(pat)+1
        t=[[None]*m for i in range(n)]
        t[0][0]=True
        for i in range(1,n):
            t[i][0]=False
        for j in range(1,m):
            t[0][j]=t[0][j-1] and pat[j-1]=="*"
        for i in range(1,n):
            for j in range(1,m):
                if txt[i-1]==pat[j-1] or pat[j-1]=="?":
                    t[i][j]=t[i-1][j-1]
                elif pat[j-1]=="*":
                    t[i][j]=t[i-1][j] or t[i][j-1]
                else:
                    t[i][j]=False
        return t[n-1][m-1]
        