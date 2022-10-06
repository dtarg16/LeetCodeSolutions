class TimeMap:

    def __init__(self):
        self.memo = {}
        self.len = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.memo:
            self.memo[key].append([timestamp, value])
            self.len[key] += 1
        else:
            self.memo[key] = [[timestamp, value]]
            self.len[key] = 1
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memo:
            return ""
        
        start = 0
        end = self.len[key] - 1
        answerIdx = -1
        while start<=end:
            mid = (start+end)//2
            
            if self.memo[key][mid][0] > timestamp:
                end = mid-1
            else:
                answerIdx = mid
                start = mid+1
            
        if answerIdx==-1:
            return ""
        
        return self.memo[key][answerIdx][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)