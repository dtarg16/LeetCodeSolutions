class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        dic = {}
        
        res = 0
        mod = 1000000007
        for i in range(len(arr)):
            res = (res + dic.get(target - arr[i], 0)) % mod
            
            for j in range(i):
                tmp = arr[i] + arr[j]
                dic[tmp] = dic.get(tmp, 0) + 1
                
        return res