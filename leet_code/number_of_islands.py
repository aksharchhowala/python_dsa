class Solution(object):
    def __init__(self) -> None:
        pass
    
    def numIslands(self, grid):
        if not grid:
            return 0
        island = 0
        for index in range(len(grid)):
            for inner in range(len(grid[index])):
                if grid[index][inner] == "1":
                    self.dfs_island(grid, index, inner)
                    island += 1
        return island
    
    def dfs_island(self, grid, index, inner):
        if not(0 <= index < len(grid)) or not(0 <= inner < len(grid[index])) or grid[index][inner] != "1":
            return
        grid[index][inner] = "#"
        self.dfs_island(grid, index + 1, inner)
        self.dfs_island(grid, index - 1, inner)
        self.dfs_island(grid, index, inner + 1)
        self.dfs_island(grid, index, inner - 1)
                    
            

if __name__ == "__main__":

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
    
    sol = Solution()
    print(sol.numIslands(grid))


