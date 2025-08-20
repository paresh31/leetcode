class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        dp = [[0] * c for i in range(r)]
        ts = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                ts += dp[i][j]
        return ts