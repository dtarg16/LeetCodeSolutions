class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3: return False

        
        l, r = 0, length
        
        for i in range(1, length):
            if arr[i] <= arr[i-1]:
                l = i-1
                break
                
        for i in range(len(arr)-2, -1, -1):
            if arr[i] <= arr[i+1]:
                r = i+1
                break
        
        return l == r