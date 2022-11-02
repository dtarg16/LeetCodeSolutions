class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        q = deque([start])
        visited = set()
        mutations = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return mutations
                if cur not in visited:
                    visited.add(cur)
                    for nei in bank:
                        if checkNeighbor(cur,nei):
                            q.append(nei)
            mutations += 1
        return -1