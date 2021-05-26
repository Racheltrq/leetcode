class Solution(object):
    def countVowelStrings(self, n):
        if n == 1:
            return 5
        if n == 2:
            return 15
        n_prev = [5,4,3,2,1]
        for i in range(3, n+1):
            n_prev[0] = sum(n_prev)
            n_prev[1] = sum(n_prev[1:])
            n_prev[2] = sum(n_prev[2:])
            n_prev[3] = sum(n_prev[3:])
            n_prev[4] = sum(n_prev[4:])
        return sum(n_prev)
        
        
