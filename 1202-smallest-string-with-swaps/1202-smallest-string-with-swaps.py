class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
  
    def find(self, x):
        if x == self.root[x]:
            return x
        return self.find(self.root[x])
  
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
    
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
    
        for left, right in pairs:
            uf.union(left, right)

        groups = defaultdict(list)
        for i in range(len(s)):
            group = uf.find(i)
            ch = s[i]
            groups[group].append(ch)

        for group in groups.keys():
            groups[group].sort(reverse=True)

        res = []
        for i in range(len(s)):
            group = uf.find(i)
            ch = groups[group].pop()
            res.append(ch)
            
        return "".join(res)