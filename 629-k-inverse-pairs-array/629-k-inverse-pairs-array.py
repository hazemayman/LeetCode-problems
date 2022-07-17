class Solution:

    def kInversePairs(self, n: int, k: int) -> int:
        lookup = [[0 for j in range(k+1)] for i in range(n+1)]
        lookup[0] = [0] * (k+1)
        m = 1000000007
        for i in range(1 , n+1):
            for j in range(0 , k+1):
                if(i == 1 and j == 0):
                    lookup[i][j] = 1 
                    break
                elif(j == 0):
                    lookup[i][j] = 1
                else:
                    val = lookup[i-1][j - i]  if j - i >= 0 else 0
                    val =  (lookup[i-1][j] - val)
                    lookup[i][j] = (lookup[i][j-1] +  val )%m                                                                                                           
                        
        return lookup[n][k]