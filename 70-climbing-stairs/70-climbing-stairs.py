class Solution:
    def climbStairs(self, n: int) -> int:
        lookup = [1 , 2]
        i = n-1
        for i in range(2 , n):
            lookup[i%2] = lookup[0] + lookup[1]
        return lookup[i%2]