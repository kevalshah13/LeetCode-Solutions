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
            ans=min(ans,diff)
        return min(ans,24*60-new[-1]+new[0])
        