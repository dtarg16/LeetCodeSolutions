class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a','A','e','E','i','I','o','O','u','U'}
        s = list(s)
        left = 0
        right = len(s)-1

        while left<right:
            
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
        	
            s[left],s[right] = s[right],s[left]
            right -= 1
            left += 1

        return ''.join(s)