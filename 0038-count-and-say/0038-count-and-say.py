class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def mapToCntArr(n):
            if n == 1:
                return [[1,1]]
            tmp = str(n)
            cnt = 1
            res = []
            for i in range(1,len(tmp)):
                if tmp[i] == tmp[i-1]:
                    cnt += 1
                else:
                    res.append([tmp[i-1],cnt])
                    cnt = 1
            res.append([tmp[-1],cnt])
            return res
        
        def pairsToInteger(arr):
            tmp = ""
            for dig , freq in arr:
                tmp += str(freq) + str(dig)
            return tmp
        
        ans = "1"
        for i in range(n-1):
            arrOfPairs = mapToCntArr(ans)
            ans = pairsToInteger(arrOfPairs)
        return ans