class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        st = []
        for i in range(len(colors)-1,-1,-1):
            if len(st)==0:
                st.append([colors[i],i])
            elif st[-1][0]!=colors[i]:
                st.append([colors[i],i])
            elif st[-1][0]==colors[i]:
                m=min(neededTime[st[-1][1]],neededTime[i])
                if m==neededTime[i]:
                    ans+=m
                else:
                    sttop = st.pop()
                    ans+=neededTime[sttop[1]]
                    st.append([colors[i],i])
        return ans