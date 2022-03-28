class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def nthPalindrome(n, k):

            if k & 1:
                temp = k // 2
            else:
                temp = k // 2 - 1

            palindrome = 10 ** temp
            palindrome = palindrome + n - 1

            ans = str(palindrome)

            if k & 1:
                palindrome = palindrome // 10

            while palindrome:
                ans += str(palindrome % 10)
                palindrome = palindrome // 10

            if len(ans) > k:
                return -1
            return int(ans)

        ans = []
        for query in queries:
            ans.append(nthPalindrome(query, intLength))

        return ans