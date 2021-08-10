class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return []
        else:
            res = []
            self.helper(n, n, res, "")
            return res
            
    def helper(self, left, right, res, string):
        
        #print(left, right, res, string)
        if right < left:
            return 
        if not left and not right:
            #print("both zero")
            res.append(string)
            return
        if left:
            self.helper(left-1, right, res, string+"(")
        if right:
            self.helper(left, right-1, res, string+")")