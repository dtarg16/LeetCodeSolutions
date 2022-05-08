class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mp = set(["2", "22", "222",
                  "3", "33", "333",
                  '4', '44', '444',
                  '5', '55', '555',
                  '6', '66', '666',
                  '7', '77', '777', '7777', 
                  '8', '88', '888', 
                  '9', '99', '999', '9999'])
        MOD = pow(10, 9) + 7
        n = len(pressedKeys)
        
        @cache
        def dp(i):
            if i>=n:
                return 1
            ans = 0
            if i+1<=n and pressedKeys[i:i+1] in mp: ans += dp(i+1)%MOD
            if i+2<=n and pressedKeys[i:i+2] in mp: ans += dp(i+2)%MOD
            if i+3<=n and pressedKeys[i:i+3] in mp: ans += dp(i+3)%MOD
            if i+4<=n and pressedKeys[i:i+4] in mp: ans += dp(i+4)%MOD
            return ans%MOD
        
        return dp(0)%MOD