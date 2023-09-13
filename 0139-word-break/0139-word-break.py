class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set([w for w in wordDict if w in s])
        
        def dfs(s):
            if s in memo:
                return memo[s]
            if s in wordSet:
                return True

            for i in range(1, len(s)):
                prefix, suffix = s[:i], s[i:]

                if prefix in wordSet and dfs(suffix):
                    memo[s] = True
                    return True
            
            memo[s] = False
            return False
        
        
        return dfs(s)
    
        