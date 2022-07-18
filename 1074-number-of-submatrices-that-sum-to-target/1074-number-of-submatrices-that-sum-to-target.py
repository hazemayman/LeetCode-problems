class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r = len(matrix)
        c = len(matrix[0])
        ans = 0
        psa = [[0 for j in range(c)] for i in range(r)]
        psa[0][0] = matrix[0][0]
        for y1 in range(0 , r):
            for x1 in range(0 , c):
                if(y1 == 0):
                    psa[0][x1] = psa[0][x1-1]+ matrix[0][x1]
                elif(x1 == 0):
                    psa[y1][0] = psa[y1-1][0] + matrix[y1][0]
                else:
                    psa[y1][x1] = psa[y1-1][x1] + psa[y1][x1-1] - psa[y1-1][x1-1] + matrix[y1][x1]


        for y1 in range(r):
            for y2 in range(y1, r):
                lookup ={0 : 1}
                for x in range(c):
                    sum = psa[y2][x]
                    if y1 > 0:
                        sum -= psa[y1-1][x]
                    if sum - target in lookup:
                        ans += lookup[sum - target]
                    if(sum in lookup):
                        lookup[sum] += 1
                    else:
                         lookup[sum] = 1
        return ans