class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        ans = 0

        for g,p in sorted(zip(growTime,plantTime)):
            ans = g + p if g >= ans else ans + p    
                                                    
        return ans                                  
                                                