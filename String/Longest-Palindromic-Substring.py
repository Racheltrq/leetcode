class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.findPalindrome(s, i, i)
            if len(odd) > len(res):
                res = odd
            if i+1 < len(s) and s[i] == s[i+1]:
                even = self.findPalindrome(s, i, i+1)
                if len(even) > len(res):
                    res = even
        return res
            
            
    
    def findPalindrome(self, s, l, r) -> str:
        #print(l, r)
        res_l = l; res_r = r
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res_l = l; res_r = r
            l -= 1; r += 1
        #print(s[res_l:res_r+1])
        return s[res_l:res_r+1]