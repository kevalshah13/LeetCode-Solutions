# import math

# class Solution:
#     def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#         count2={}
#         for i in words2:
#             for j in i:
#                 count2[j]=count2.get(j,0)+1
#         print(count2)
#         for i in count2:
#             if count2[i]!=0:
#                 count2[i]=math.ceil(count2[i]/len(words2))
#         print(count2)
#         ans=[]
#         for w in words1:
#             count1={}
#             for i in w:
#                 count1[i]=count1.get(i,0)+1
#             print(count1)
#             for j in count2:
#                 if(j in count1 and count2[j]<=count1[j]):
#                     ans.append(w)
            
#         return w
class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans