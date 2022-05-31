class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_k_substrings = {s[i:i + k] for i in range(len(s) - k + 1)}
        
        return len(all_k_substrings) == 2 ** k