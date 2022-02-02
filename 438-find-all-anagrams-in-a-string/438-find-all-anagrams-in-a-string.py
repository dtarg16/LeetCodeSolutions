class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)
        ans = []
        if len_p > len_s:
            return ans
        if len_p == 0:
            return list(range(len_s))
        
        ft = {}
        for letter in p:
            ft[letter] = ft.get(letter, 0) + 1
        
        fm = {}
        for i in range(len_p - 1):
            fm[s[i]] = fm.get(s[i], 0) + 1       
            
        for i in range(len_p - 1, len_s):
            letter = s[i]
            fm[letter] = fm.get(letter, 0) + 1       
            
            if i != len_p -1:
                fm[s[i - len_p]] -= 1
            
            all_match = True
            for letter, freq in ft.items():
                if freq != fm.get(letter, 0):
                    all_match = False
                    break
            if all_match:
                ans.append(i - len_p + 1)
                    
        return ans