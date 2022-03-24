class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l, r = 0, n - 1
        while l < r:
            left, right = people[l], people[r]
            if left + right <= limit:
                l += 1
                n -= 1
            r -= 1
            
        return n