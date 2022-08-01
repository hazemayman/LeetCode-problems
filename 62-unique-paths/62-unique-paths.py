class Solution:
    lookup = [[-1 for i in range(101)] for i in range(101)]
    def uniquePaths(self, m: int, n: int) -> int:
        if(m <=0 or n <= 0): return 0
        if(self.lookup[m][n] != -1):return self.lookup[m][n]
        if(n == 1 or m == 1):
            self.lookup[m][n] = 1
            return 1
        output = self.uniquePaths(m-1 , n) + self.uniquePaths(m , n-1)
        self.lookup[m][n] = output
        return output
        