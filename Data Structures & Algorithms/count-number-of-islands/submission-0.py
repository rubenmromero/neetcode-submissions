class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLUMNS = len(grid), len(grid[0])
        islands = 0

        def dfs(row, column):
            if (row < 0 or column < 0 or row >= ROWS or
                column >= COLUMNS or grid[row][column] == "0"
            ):
                return

            grid[row][column] = "0"
            for drow, dcolumn in directions:
                dfs(row + drow, column + dcolumn)

        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column] == "1":
                    dfs(row, column)
                    islands += 1

        return islands