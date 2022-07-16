class Solution:
    lookup = None
    m = None
    n = None
    def rec(self , r , c , moves):
        if (r < 0 or r>=self.m or c<0 or c>=self.n):
            return 1
        if(moves == 0):
            return 0
        key = (r + moves*self.m)*self.n + c
        if(key in self.lookup):
            return self.lookup[key]
        answer = self.rec(r-1,c,moves-1) + self.rec(r,c-1,moves-1) + self.rec(r+1,c,moves-1) + self.rec(r,c+1,moves-1)
        self.lookup[key] = answer
        return answer
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m = m
        self.n = n
        self.lookup = {}
        r = self.rec(startRow,startColumn,maxMove)
        # print(self.lookup)
        # return r 
        return (r % (pow(10,9) + 7))
        