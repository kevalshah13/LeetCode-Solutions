class Solution:
	def kInversePairs(self, n: int, k: int) -> int:
		m = 10 ** 9 + 7

		dp0 = [0] * (k + 1)
		dp0[0] = 1

		for i in range(n):
			dp1 = []
			s = 0
			for j in range(k + 1):
				s += dp0[j]
				if j >= i + 1:
					s -= dp0[j - i - 1]
				s %= m
				dp1.append(s)
			dp0 = dp1
		return dp0[-1]

# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:

        # m=max(n,k)
        # dp=[[0 for j in range(m+1)] for i in range(m+1)]
        # dp[0][0]=1
        # # dp[1][0]=dp[1][1]=1
        # # dp=[]
        # m=10**9+7
        # for i in range(1,n+1):
        #     temp=[]
        #     for j in range(i+1):
        #         if(j==0 or j==i-1):
        #             temp.append(1)
        #         else:
        #             temp.append(0)
        #     dp.append(temp)
        # print(dp)
        # for i in range(1, n + 1):
        #     for j in range(0, k + 1):
        #         for x in range(0, min(j, i - 1) + 1):
        #             if j - x >= 0:
        #                 dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % 1000000007

        # return dp[n][k]
        # # for i in range(2,n):
        # #     for j in range(1,i):
        # #         # print(i,j)
        # #         dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%m

        # print(dp)
        # return dp[n-1][k]
        