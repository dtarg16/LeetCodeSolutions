class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's voting algo
        
        candidate = None
        counter = 0
        for num in nums:
            if counter == 0:
                candidate = num
                counter += 1
            else:
                if num == candidate:
                    counter += 1
                else:
                    counter -= 1
                    
        return candidate
            