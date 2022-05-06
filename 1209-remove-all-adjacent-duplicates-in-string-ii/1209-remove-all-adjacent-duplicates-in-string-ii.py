class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for ch in s:
            if not stk:
                stk.append([ch, 1])
            
            else:
                if stk[-1][0] == ch:
                    stk[-1][1] +=1 

                    if stk[-1][1] == k:
                        stk.pop()
                else:
                    stk.append([ch, 1])
                
        res = ""
        for ch, count in stk:
            res += ch * count
            
        return res
        
        