class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        res = []
        for i in range(len(l)):
            left = l[i]
            right = r[i]
            subarray = nums[left: right + 1]
            subarray.sort()
            if(right - left > 0):
                interval = subarray[1] - subarray[0]
                j = 0
                while(j < right-left):
                    #print("left:", left, "right:", right, "j:", j, subarray)
                    if subarray[j+1] - subarray[j] != interval:
                        res.append(False)
                        break
                    j += 1
                if len(res) == i:
                    res.append(True)
                    
            
            else:
                res.append(False)
            #print(res)
        return res