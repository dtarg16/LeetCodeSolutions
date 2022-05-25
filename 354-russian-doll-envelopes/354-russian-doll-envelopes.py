class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        heights, lis = [h for w, h in envelopes], []
        for h in heights:
            idx = bisect.bisect_left(lis, h)
            lis[idx:idx+1] = [h]
        return len(lis)
                
        
        