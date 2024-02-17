class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # prepare: use a min heap to store each difference(climb) between two contiguous buildings
        # strategy: use the ladders for the longest climbs and the bricks for the shortest climbs
        
        min_heap = []
        n = len(heights)
        
        for i in range(n-1):
            climb = heights[i+1] - heights[i]
            
            if climb <= 0:
                continue
            
            # we need to use a ladder or some bricks, always take the ladder at first
            if climb > 0:
                heapq.heappush(min_heap, climb)
            
            # ladders are all in used, find the current shortest climb to use bricks instead!
            if len(min_heap) > ladders:
                # find the current shortest climb to use bricks
                brick_need = heapq.heappop(min_heap)
                bricks -= brick_need
            
            if bricks < 0:
                return i
        
        return n-1

# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         diff=[0]
#         curr=0
#         ladders2,bricks2=ladders,bricks
#         for i in range(len(heights)-1):
#             if(heights[i+1]>heights[i]):
#                 curr+=heights[i+1]-heights[i]
#             diff.append(curr)
#         print(diff)
#         i=0
#         while(i<len(diff)-1):
#             if(diff[i+1]>diff[i]):
#                 if(bricks<=0 and ladders<=0):
#                     # print(i,"abc")
#                     break
#                 if(bricks>=diff[i+1]-diff[i]):
#                     bricks-=diff[i+1]-diff[i]
#                 else:
#                     ladders-=1
#             i+=1
#         print(i)
#         j=0
#         while(j<len(diff)-1):
#             if(diff[j+1]>diff[j]):
#                 if(bricks2<=0 and ladders2<=0):
#                     # print(i,"abc")
#                     break
#                 if(ladders2>0):
#                     ladders2-=1
#                 else:
#                     bricks2-=diff[j+1]-diff[j]
#             j+=1
#         print(j)


#         return max(i,j)