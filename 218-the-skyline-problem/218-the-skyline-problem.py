class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        positions = sorted(set([left for left, _, _ in buildings] + [right for _, right, _ in buildings]))

        ptr, prevH = 0, 0
        alive, ret = [], []
        
        for curPos in positions:
            while alive and alive[0][1] <= curPos:
                heappop(alive)
            
            while ptr < len(buildings) and buildings[ptr][0] <= curPos:
                heappush(alive, [-buildings[ptr][2], buildings[ptr][1]])
                ptr += 1
            
            if alive:
                curH = -alive[0][0]
                if curH != prevH:
                    ret.append([curPos, curH])
                    prevH = curH
            else:  
                ret.append([curPos, 0])
                
        return ret