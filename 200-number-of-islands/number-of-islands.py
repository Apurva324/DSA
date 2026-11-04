class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[0] * m for _ in range(n)]
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        def is_valid(row, col):
            if row < 0 or row >= n or col < 0 or col >= m:
                return False
            return True
        
        def dfs(row,col):
            visited[row][col] = 1
            for k in range(0,4):
                new_row = row + x[k]
                new_col = col + y[k]
                if (is_valid(new_row, new_col) and grid[new_row][new_col] == '1' and
                    visited[new_row][new_col] == 0):
                    dfs(new_row, new_col)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    res += 1
                    dfs(i,j)
        return res
        