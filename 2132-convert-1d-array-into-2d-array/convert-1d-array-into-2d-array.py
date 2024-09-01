class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        r,c=0,0
        if(len(original)!=m*n):
            return []
        ans = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            if(c>=n and r<m):
                r+=1
                c=0
            if(r>=m):
                # if(i<len(original)):
                #     return []
                return ans
            else:
                ans[r][c]=original[i]
                c+=1
        
        return ans
        