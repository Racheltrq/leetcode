class Solution(object):
    def findCenter(self, edges):
        if len(edges) < 2:
            return None;
        num1 = edges[0][0]
        num2 = edges[0][1]
        if num1 in edges[1]:
            return num1
        if num2 in edges[1]:
            return num2
        return None