class Solution:
    def backspaceCompare(self, S, T):
        def stack(s):
            stack = []
            for char in s:
                if char is not "#":
                    stack.append(char)
                else:
                    if not stack:
                        continue
                    stack.pop()
            return stack
        
        l1 = stack(S)
        l2 = stack(T)
        return l1 == l2
        
    
    
        