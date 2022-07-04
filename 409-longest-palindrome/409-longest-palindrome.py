class Solution:
    def longestPalindrome(self, s: str) -> int:
        visited = set()
        for c in s:
            if c not in visited:
                visited.add(c)
            else:
                visited.remove(c)
        
        if len(visited) > 0:
            return len(s) - len(visited) + 1
        
        return len(s)