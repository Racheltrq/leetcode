class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        nums.sort()
        return self.helper(nums, [], [])
        
    def helper(self, nums, res, curRes):
        if len(nums) == 1:
            curRes.append(nums[0])
            if curRes not in res: 
                res.append(curRes)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.helper(nums[:i]+nums[i+1:], res, curRes+[nums[i]])
        return res