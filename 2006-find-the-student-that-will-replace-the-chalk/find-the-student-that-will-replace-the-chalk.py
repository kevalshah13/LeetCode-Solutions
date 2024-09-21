# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         i=0
#         n=len(chalk)
#         while(k>0):
#             if(k-chalk[i]<0):
#                 return i
#             k-=chalk[i]
#             i=(i+1)%n
#         return i

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Find the sum of all elements.
        sum_chalk = 0
        for i in range(len(chalk)):
            sum_chalk += chalk[i]
            if sum_chalk > k:
                break
        # Find modulo of k with sum.
        k = k % sum_chalk
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0