class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        clossed = -1
        for i in range(len(matrix[0])):
            if(matrix[0][i] == target):
                return True
            elif(matrix[0][i] > target):
                break
            clossed = i
        
        for c in range(i , -1 , -1):
            for r in range(len(matrix)):
                if(matrix[r][c] == target):return True
                if(matrix[r][c] > target): break
      
        return False