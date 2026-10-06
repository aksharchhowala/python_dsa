class Solution(object):
    def __init__(self) -> None:
        self.visited = set()
        self.number_of_islands = 0
        
    def numIslands(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in self.visited:
                    if "1" not in grid[i]:
                        break
                    if grid[i][j] == "1":
                        if not (i,j) in self.visited:
                            self.dsa(grid, i, j)
                            self.number_of_islands += 1
                
                
        return self.number_of_islands
        
    def dsa(self, arr, i, j):
        if 0 <= i < len(arr) and 0 <= j < len(arr[i]):
            if (i,j) not in self.visited:
                if arr[i][j] == "1":
                    self.visited.add((i,j))
                    self.dsa(arr, i, j+1)
                    self.dsa(arr, i, j-1)
                    self.dsa(arr,i+1, j)
                    self.dsa(arr, i-1, j)
            

if __name__ == "__main__":

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
    
    sol = Solution()
    print(sol.numIslands(grid))


