class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        for i in range(1,10):
            num,rem=i,i
            while(num<=high and rem<10):
                if(num>=low and num<=high):
                    ans.append(num)
                num=(num*10)+(rem+1)
                rem+=1
        return sorted(ans)
        
    
