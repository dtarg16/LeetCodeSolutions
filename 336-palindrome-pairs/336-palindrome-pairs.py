class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        idx_map = {}
        for i, word in enumerate(words):
            idx_map[word] = i
            
        res = set()
        for i, word in enumerate(words):
            if not word:
                continue

            for j in range(len(word)):
                current = word[:j]
                target = word[j:][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    res.add((idx_map[target], i))
                    
            for j in range(len(word), -1, -1):
                current = word[j:]
                target = word[:j][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    res.add((i, idx_map[target]))

            if word == word[::-1] and "" in idx_map:
                idx = idx_map[""]
                res.add((i, idx))
                res.add((idx, i))

        return list(res)