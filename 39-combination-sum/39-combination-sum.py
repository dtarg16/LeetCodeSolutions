class Solution:
    
    
    def rec(self, index, current_list, current_sum):
        if current_sum > self.target or index >= len(self.candidates):
            return
        if current_sum == self.target:
            self.ans.append(current_list)
            return

        candidate = self.candidates[index]
        self.rec(index, current_list + [candidate], current_sum + candidate)
        self.rec(index + 1, current_list, current_sum)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.candidates = candidates
        self.target = target
        self.rec(0, [], 0)
        return self.ans