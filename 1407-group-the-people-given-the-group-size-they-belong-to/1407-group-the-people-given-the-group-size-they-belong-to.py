class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        output = []
        n = len(groupSizes)
        for i in range(n):
            gs = groupSizes[i]
            group = groups.get(gs, [])
            group.append(i)
            if len(group) == gs:
                output.append(group)
                group = []
            groups[gs] = group
            
        return output