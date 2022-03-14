class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        
        for p in path.split('/'):
            
            if stk and p == '..':
                stk.pop()
                    
            elif p and p != '.' and p != '..':
                stk.append(p)
                
        return '/' + '/'.join(stk)
                