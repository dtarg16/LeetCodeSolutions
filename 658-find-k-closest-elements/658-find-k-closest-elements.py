class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k==len(arr):
            return arr
        i=0
        j=k
        
        while (j<len(arr)):
            if (abs(arr[i]-x)>abs(arr[j]-x) or arr[i]==arr[j]):
                i+=1
                j+=1
            else:
                break
                
        newArr=arr[i:j]
        return newArr