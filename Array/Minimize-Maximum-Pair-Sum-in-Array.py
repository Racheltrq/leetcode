class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        curL = 0
        res = 0
        while(curL < len(nums) - 1 - curL):
            temp = nums[curL] + nums[len(nums) - 1 - curL]
            if temp > res:
                res = temp
            curL += 1
        return res