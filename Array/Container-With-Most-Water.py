class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointerL = res = 0
        pointerR = len(height) - 1
        while pointerR > pointerL:
            tmp = (pointerR - pointerL) * min(height[pointerL], height[pointerR])
            #print(height[pointerL], height[pointerR], tmp)
            if tmp > res:
                res = tmp
            if height[pointerL] < height[pointerR]:
                pointerL += 1
            else:
                pointerR -= 1
            
        return res