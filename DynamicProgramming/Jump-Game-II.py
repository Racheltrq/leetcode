class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jump = 1
        farthest = curr_farthest = nums[0]
        if nums[0] + 1 >= len(nums):
            return 1
        ind = 1
        while curr_farthest < len(nums) - 1 and ind + 1 < len(nums):
            while ind <= curr_farthest and ind < len(nums):
                if ind + nums[ind] > farthest:
                    farthest = ind + nums[ind]
                ind += 1
            jump += 1
            curr_farthest = farthest
        return jump