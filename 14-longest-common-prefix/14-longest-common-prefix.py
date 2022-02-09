class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if len(strs) == 0:
            return res
        
        min_len = len(min(strs, key=len))
        
        for i in range(min_len):
            ch = strs[0][i]
            for str in strs:
                if str[i] != ch:
                    return res
                
            res += ch
            
        return res