class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        lpointer = 0
        rpointer = 1    
        dict ={}
        dict[s[0]] = 0
        res = 1
        while rpointer < len(s):
            #print(dict, lpointer, rpointer)
            if s[rpointer] not in dict:
                dict[s[rpointer]] = rpointer
                if rpointer - lpointer + 1 > res:
                    res = rpointer - lpointer + 1
            else:
                lpointer_new = dict[s[rpointer]] + 1
                while lpointer < lpointer_new:
                    #print("-popping:", s[lpointer])
                    dict.pop(s[lpointer], None)
                    lpointer += 1
                #print("-adding:", s[lpointer])
                dict[s[rpointer]] = rpointer
            rpointer += 1
            #print("cur longest:", res)
        return res
