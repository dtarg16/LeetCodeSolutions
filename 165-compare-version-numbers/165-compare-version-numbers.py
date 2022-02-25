class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(v) for v in version1.split(".")]
        version2 = [int(v) for v in version2.split(".")]
        print(version1, version2)
        for i in range(max(len(version1),len(version2))):
            if i < len(version1):
                v1 = version1[i]
            else :
                v1 = 0
            if i < len(version2):
                v2 = version2[i]
            else :
                v2 = 0
                
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0