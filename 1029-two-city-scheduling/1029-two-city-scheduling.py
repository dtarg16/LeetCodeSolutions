class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_a = sum([a for a, b in costs])
        differences = sorted([b - a for a, b in costs])
        cost_b = sum(differences[: len(costs) // 2])
        return cost_a + cost_b