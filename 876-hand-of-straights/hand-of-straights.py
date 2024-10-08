class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Step 1: Check if grouping is possible
        if len(hand) % groupSize != 0:
            return False
        
        # Step 2: Count the occurrences of each card
        count = Counter(hand)
        
        # Step 3: Sort the unique card values
        sorted_keys = sorted(count.keys())
        
        # Step 4: Form consecutive groups
        for key in sorted_keys:
            if count[key] > 0:  # If this card is still available
                start_count = count[key]
                # Check and form a group starting from `key`
                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        
        # Step 5: Return True if all groups are formed successfully
        return True
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         mem=[0]*max(hand)
#         for i in hand:
#             mem[i-1]=1+mem[i-1]
#         print(mem)
#         if(len(hand)%groupSize!=0):
#             return False
#         else:
#             while(sum(mem)!=0):
#                 j=0
#                 for i in range(j,j+groupSize):
#                     print(i,mem)
#                     if(hand[i]==0):
#                         break
#                         j+=1
#                     else:
#                         mem[i]-=1
#                         j+=1
#                 print("loop ends")
#                 if(j==len(mem)-1):
#                     return False
#         return 0