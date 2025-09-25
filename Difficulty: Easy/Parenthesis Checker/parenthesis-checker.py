class Solution:
    def isBalanced(self, s):
        # code here
        stack=[]
        pairs={']':'[',')':'(','}':'{'}
        for b in s:
            if b in pairs.values():
                stack.append(b)
            elif b in pairs:
                if not stack or stack[-1]!=pairs[b]:
                    return False
                else:
                    stack.pop()
                    
        return len(stack)==0
                    
                
        
        