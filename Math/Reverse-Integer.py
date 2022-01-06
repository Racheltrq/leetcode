class Solution:
    def reverse(self, x: int) -> int:
        length = 0
        lst = []
        invert = False
        if x < 0:
            invert = True
            x = -x
        while x >= 10:
            lst.append(x%10)
            x = x // 10
            length += 1
        lst.append(x)
        length += 1
        res = 0
        #print(lst)
        for i in lst:
            if i == 0:
                length -= 1
                continue
            res += i * pow(10, length - 1)
            length -= 1
            #print(i, res)
        
        if res > pow(2, 31) - 1 or res < -pow(2, 31):
            return 0
            
        if invert:
            return -res
        else:
            return res