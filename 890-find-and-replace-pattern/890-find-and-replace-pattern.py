class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def F(word):
            m = {}
            return [m.setdefault(c, len(m)) for c in word]
        return [word for word in words if F(word) == F(pattern)]