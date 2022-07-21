class Solution:
    lookup = {}
    def climbStairs(self, n: int) -> int:
        lookup = [1 , 2]
        for i in range(2 , n):
            lookup.append(lookup[i-1] + lookup[i-2])
        return lookup[n-1]