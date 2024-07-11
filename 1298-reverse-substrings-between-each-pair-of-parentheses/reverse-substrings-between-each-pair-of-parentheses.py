class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(l, r):
            while l < r:
                ch[l], ch[r] = ch[r], ch[l]
                l += 1
                r -= 1
        stack = []
        ch = list(s)
        for i, c in enumerate(ch):
            if c == '(':
                stack.append(i)
            elif c == ')':
                reverse(stack.pop(), i)
        return ''.join([c for c in ch if c.isalpha()])


# from collections import defaultdict
# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         m=defaultdict(list)
#         for i in range(len(s)):
#             if s[i]=="(" or s[i]==")":
#                 m[s[i]].append(i)
#         print(m)
#         n=len(m["("])
#         s1=s
#         c=0
#         for i in range(n):
#             s1=s1[:m["("][n-1-i]]+s1[m[")"][i]-1-c:m["("][n-1-i]:-1]+s1[m[")"][i]+1-c:]
#             c+=2
#             print(s1)
#         return s1
        