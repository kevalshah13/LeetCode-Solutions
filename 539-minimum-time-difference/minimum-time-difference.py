class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        new=[]
        for i in timePoints:
            h,m=i.split(':')
            new.append(int(h)*60+int(m))
        new.sort()
        print(new)
        ans=24*60
        for i in range(1,len(new)):
            diff=new[i]-new[i-1]
        #     # if(new[i][0]<=12):
        #     diff=(new[i][0]-new[i-1][0])*60+(new[i][1]-new[i-1][1])
        #     # if(diff>=12*60):
        #     #     diff=abs(1440-diff)
            ans=min(ans,diff)
        #     print(ans)
        # ans=min(ans,abs((new[0][0]-new[len(new)-1][0])*60+(new[0][1]-new[len(new)-1][1])))
        return min(ans,24*60-new[-1]+new[0])
        