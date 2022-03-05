class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        dic = {}
        for i in range(len(mapping)):
            dic[i] = mapping[i]

        def cmp(x, y):
            return mapp(x) - mapp(y)

        def mapp(num):
            if num in dic:
                return dic[num]

            right = int(str(num)[-1])
            mapped_right = dic[right]
            mapped_left = mapp(num//10)
            ans = mapped_left*10 + mapped_right
            dic[num] = ans
            return ans
        
        return sorted(nums, key=cmp_to_key(cmp))