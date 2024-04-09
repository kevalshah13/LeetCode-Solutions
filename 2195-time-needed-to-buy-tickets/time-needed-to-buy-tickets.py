class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total=0
        for i in range(len(tickets)):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)
        return total
        # time=[0]*len(tickets)
        # while(tickets[k]!=0):
        #     for i in range(len(tickets)):
        #         if(tickets[i]>0):
        #             time[i]+=1
        #             tickets[i]-=1
        # print(time)
        # return sum(time)