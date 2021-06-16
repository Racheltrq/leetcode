class Solution(object):
    def calculate_mat(self, m, n, row, col, mat):
        if row == m - 1 or col == n - 1:
            mat[row][col] = 1
        else:
            mat[row][col] = mat[row + 1][col] + mat[row][col + 1]
            
            
    def uniquePaths(self, m, n):
        mat = [[0] * n for i in range(m)]
        
        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                self.calculate_mat(m, n, x, y, mat)
        return mat[0][0]