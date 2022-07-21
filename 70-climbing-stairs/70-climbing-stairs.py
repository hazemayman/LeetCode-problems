class Solution:
    lookup = {}
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        if(n in self.lookup):
            return self.lookup[n]
        value = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.lookup[n] = value
        return value