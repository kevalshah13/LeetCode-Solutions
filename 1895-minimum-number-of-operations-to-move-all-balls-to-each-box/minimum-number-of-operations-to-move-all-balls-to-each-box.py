class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        ans=[0]*n

        LeftBall,RightBall = 0,0
        LeftMoves,RightMoves = 0,0

        for i in range(n):
            ans[i]+= LeftMoves
            LeftBall += int(boxes[i])
            LeftMoves += LeftBall

            j = n-i-1
            ans[j]+=RightMoves
            RightBall +=int(boxes[j])
            RightMoves += RightBall
        return ans
