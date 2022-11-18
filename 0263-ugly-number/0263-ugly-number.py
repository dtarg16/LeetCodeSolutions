class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0: 
            return False
        @cache
        def dfs(cur):
            if cur==n: 
                return True
            if cur>n: 
                return False
            for k in (5,3,2):
                if dfs(cur*k): 
                    return True
        return dfs(1)