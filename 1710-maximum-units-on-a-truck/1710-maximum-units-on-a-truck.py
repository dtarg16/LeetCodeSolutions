class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        totalUnits, i = 0, 0
        
        while truckSize and i < len(boxTypes):
            numBoxes, numUnits = boxTypes[i]    
            n = min(truckSize, numBoxes)
            
            totalUnits += n * numUnits
            truckSize -= n
            
            i += 1
            
        return totalUnits
            