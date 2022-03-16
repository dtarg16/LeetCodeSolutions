class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stk = []
        for pop in popped:
            while True:
                if stk:
                    if stk[-1] == pop:
                        stk.pop()
                        break
 
                if not stk or stk[-1] != pop:
                    if pushed:
                        stk.append(pushed.pop(0))
                    else:
                        return False
        return True