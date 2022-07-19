class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if(numRows > 1):
            triangle.append([1,1])
            
        for i in range(1 , numRows-1):
            a = [1,1]
            a[1:1] = [sum(triangle[i][k-1:k+1]) for k in range(1 , i+1)]
            triangle.append(a)
        return triangle
            
            