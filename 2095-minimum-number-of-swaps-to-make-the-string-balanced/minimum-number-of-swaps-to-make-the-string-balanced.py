# class Solution:
#     def minSwaps(self, s: str) -> int:
#         count={}
#         ans=0
#         for i in s:
#             count[i]=1+count.get(i,0)
#             if(count[']']>count['[']):
#                 r=len(s)-1
#                 while(r>0 and s[r]!='['):
#                     r-=1
#                 s[i],s[r]=s[r],s[i]
#                 count[i]-=1
#                 count['[']+=1
#                 ans+=1

#         return len(stack)//2
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = deque()
        unbalanced = 0
        for ch in s:
            # If an opening bracket is encountered, push it in the deque.
            if ch == "[":
                stack.append(ch)
            else:
                # If the deque is not empty, pop it.
                if stack:
                    stack.pop()
                # Otherwise increase the count of unbalanced brackets.
                else:
                    unbalanced += 1
        return (unbalanced + 1) // 2