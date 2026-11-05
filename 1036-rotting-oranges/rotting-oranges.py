class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]
        fresh = 0
        time = 0
        queue = deque()

        def is_valid(row, col):
            if row < 0 or row >= n or col < 0 or col >= m:
                return False
            return True
        
        for i in range(0, (n)):
            for j in range(0, (m)):
                if grid[i][j] == 2: # rotten tomatoes
                    queue.append((i,j))
                    grid[i][j] = -2
                else:
                    if grid[i][j] == 1:
                        fresh += 1

        while queue and fresh > 0:
            time += 1
            s = len(queue)

            while s > 0:
                r, c = queue.popleft()

                for k in range(0,4):
                    new_row = r + x[k]
                    new_col = c + y[k]

                    if is_valid(new_row, new_col) and grid[new_row][new_col] == 1:
                        queue.append((new_row,new_col))
                        grid[new_row][new_col] = -2
                        fresh -= 1
    
                s -=1 

        if fresh > 0:
            return -1 
        return time