class Solution:
    def returnMax(self,grid , i , j):
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]==0):
            return 0
        grid[i][j] = 0
        return 1 + self.returnMax(grid , i-1 , j) + self.returnMax(grid , i+1 , j) + self.returnMax(grid , i , j-1) + self.returnMax(grid , i , j+1)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1): 
                    answer = max(answer , self.returnMax(grid , i , j))
        return answer