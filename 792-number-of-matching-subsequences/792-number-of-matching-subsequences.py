class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isMatch(word, w_i, d_i):
            if w_i == len(word): 
                return True
            l = dict_idxs[word[w_i]]
            
            if len(l) == 0 or d_i > l[-1]:
                return False
            
            i = l[bisect_left(l, d_i)]
            
            return isMatch(word, w_i + 1, i + 1)

        dict_idxs = defaultdict(list)
        
        for i in range(len(s)):
            dict_idxs[s[i]].append(i)
        
        return sum(isMatch(word, 0, 0) for word in words)