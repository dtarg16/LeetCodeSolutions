class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.isupper():
            return True
        
        if word[0].isupper():
            return word[1::].islower()
        
        return False