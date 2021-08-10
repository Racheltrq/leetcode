class Solution(object):
    def trap(self, height):
        indexL = 0
        indexR = len(height) - 1
        maxL = height[indexL]
        maxR = height[indexR]
        totalWater = 0
        while indexL < indexR:
            #print(indexL, indexR)
            delta = 0
            if maxL < maxR:
                indexL += 1
                maxL = max(maxL, height[indexL])
                delta = maxL - height[indexL]
            else:
                indexR -= 1
                maxR = max(maxR, height[indexR])
                delta = maxR - height[indexR]
            if delta > 0:
                #print(delta)
                totalWater += delta
        return totalWater
                
        