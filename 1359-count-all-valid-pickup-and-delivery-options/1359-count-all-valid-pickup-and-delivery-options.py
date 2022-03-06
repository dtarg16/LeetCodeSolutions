class Solution:
    def countOrders(self, n: int) -> int:
        permutations = math.factorial(n * 2)
        valid_permutation = permutations >> n
        return valid_permutation % (10**9 + 7)