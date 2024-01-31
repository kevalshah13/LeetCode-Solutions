class Solution:
    def validateStackSequences(self, pushed, popped):
        i = j = 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i, j = i - 1, j + 1
            i += 1
        return i == 0

# class Solution:
#     def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:    
#         i=1
#         stack=[pushed[0]]
#         while(stack and i<len(pushed)):
#             while(i<len(pushed) and stack[-1]!=popped[0]):
#                 stack.append(pushed[i])
#                 i+=1
#             print(stack)
#             del popped[0]
#             stack.pop()
#         while(stack):

#         print(i,popped)
#         return not popped
        # stack=[]
        # i=0
        # while(pushed[i]!=popped[0]):
        #     stack.append(pushed[i])
        #     i+=1
        # print(stack)
        # return 0