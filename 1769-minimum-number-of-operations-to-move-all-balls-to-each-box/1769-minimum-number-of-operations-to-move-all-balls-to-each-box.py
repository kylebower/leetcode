class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        answer = [0]*n
        
        # dynamic programming solution
        
        # leftDist[i] is distance to move all balls to the left of box[i] into box i
        # leftBallCnt is the number of balls in box i after moving all the balls left of box i into box i
        leftDist = [0]*n
        leftBallCnt = int(boxes[0])
        for i in range(1,n):
            leftDist[i] = leftBallCnt + leftDist[i-1]
            leftBallCnt += int(boxes[i])
            
        # do same from right
        rightDist = [0]*n
        rightBallCnt = int(boxes[n-1])
        for i in range(n-2,-1,-1):
            rightDist[i] = rightBallCnt + rightDist[i+1]
            rightBallCnt += int(boxes[i])
        
        # compute result by moving all balls to the left of box i into box i 
        # and moving all balls to the right of box i into box i
        for i in range(n):
            answer[i] = leftDist[i] + rightDist[i]
            
        # return result
        return answer
    