class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if(numRows > 1):
            triangle.append([1,1])
            
        for i in range(1 , numRows-1):
            a = [1] * (i+2)
            k = 1
            while(k<=i):
                a[k] = sum(triangle[i][k-1:k+1])
                k+=1
            triangle.append(a)
        print(triangle)
        return triangle
            
            