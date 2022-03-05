class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dic = {}
        maxx = 0
        max_target = 0
        for i in range(0, len(nums) - 1):
            target = nums[i + 1]
            if nums[i] == key:
                dic[target] = dic.get(target, 0) + 1
                if dic[target] > maxx:
                    maxx = dic[target]
                    max_target = target
        return max_target