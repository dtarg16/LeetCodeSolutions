class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: 
            return True
        if n % 2==1: 
            return False 
       
        mn = 1
        mx = 31
        mdl = 16
        
        while mx - mn > 1:
            mdl_n = 2 << (mdl - 1)
            if n == mdl_n: 
                return True
            if n == 2 << (mx - 1): 
                return True
            if n == 2 << (mn - 1): 
                return True
            
            if n > mdl_n:
                mn = mdl
                mdl = (mdl + mx) // 2
                
            if n < mdl_n:
                mx = mdl
                mdl = (mdl + mn) // 2
        
        return False