class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            longest = max(expand(i, i), expand(i, i + 1), longest, key=lambda x: len(x))

            # palindrome1 = expand(i, i)
            # palindrome2 = expand(i, i + 1)

            # if len(palindrome1) > len(longest):
            #     longest = palindrome1
            # if len(palindrome2) > len(longest):
            #     longest = palindrome2

        return longest