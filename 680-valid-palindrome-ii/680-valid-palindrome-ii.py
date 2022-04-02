class Solution:

    def validPalindrome(self, s: str) -> bool:

        left, right, count_left = 0, len(s) - 1, 0

        while left < right:
            if s[left] == s[right]:
                right -= 1
            else:
                count_left += 1

            left += 1

            if count_left > 1:
                break

        left, right, count_right = 0, len(s) - 1, 0

        while left < right:
            if s[left] == s[right]:
                left += 1
            else:
                count_right += 1

            right -= 1

            if count_right > 1:
                break

        if count_left <= 1 or count_right <= 1:
            return True

        return False
