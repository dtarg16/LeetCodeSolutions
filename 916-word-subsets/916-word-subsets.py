class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt = Counter()
        for b in words2:
            cnt |= Counter(b)
            
        return [a for a in words1 if not cnt - Counter(a)]