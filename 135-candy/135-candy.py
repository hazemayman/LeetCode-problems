class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        leftToRight =  [0]*n
        rightToLeft = [0]*n
        for i in range(n):
            if(i != 0 and ratings[i] > ratings[i-1]):
                leftToRight[i] = leftToRight[i-1] + 1
            else:
                leftToRight[i] = 1
            
            if(i != 0 and ratings[n-i-1] > ratings[n-i]):
                rightToLeft[n-i-1] = rightToLeft[n-i] + 1
            else:
                rightToLeft[n-i-1] = 1

        total = 0
        for i in range(n):
            a = max(rightToLeft[i] , leftToRight[i])
            total+=a
            
        return total