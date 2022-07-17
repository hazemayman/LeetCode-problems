class Solution:

    def kInversePairs(self, n: int, k: int) -> int:
        lookup = [[0 for j in range(k+1)] for i in range(n+1)]
        lookup[0] = [0] * (k+1)
        m = 1000000007
        for i in range(1 , n+1):
            j = 0
            while(j <= k and j <= i * (i - 1) / 2):
                if(j == 0):
                    lookup[i][j] = 1
                else:
                    val = lookup[i-1][j - i]  if j - i >= 0 else 0
                    lookup[i][j] = (lookup[i][j-1] +  lookup[i-1][j] -val )%m
                j+=1
                        
        return lookup[n][k]