class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        for i in range(1,10):
            num=i
            rem=i
            while(num<=high and rem<10):
                if(num>=low and num<=high):
                    ans.append(num)
                num=(num*10)+(rem+1)
                rem+=1
                
            # print(ans)
        return sorted(ans)
        
        
        
        # t=str(low)[0]
        # n=len(str(low))
        # for i in range(1,n):
        #     t+=str(int(t[i-1])+1)
        # print(t)
        # ans=[int(t)]
        # while(int(t)<=high):


        # while(int(t)<=high):
        #     while(len(t)<len(str(high))):
        #         t+=str(int(t[-1])+1)
        #         print(t,'11')
        #     t=t[:-1]
        #     t=t[1:]+str(int(t[-1])+1)
        #     print(t)
        #     ans.append(int(t))
        # return ans
        
    
