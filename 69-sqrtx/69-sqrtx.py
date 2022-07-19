class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 : return 0
        if x == 1 : return 1
        minimum = 1
        maximum = x
        dm = 8
        while(dm > 1):
            temp = maximum / dm
            if(temp * temp <= x+1):
                dm-=1
            else:
                maximum = temp 
        dm = 8
        while(dm > 1):
            temp = minimum * dm
            if(temp * temp >= x -1):
                dm-=1
            else:
                minimum = temp
        while(int(maximum) != int(minimum)):
            middle = (maximum + minimum) / 2
            result = middle * middle
            if(result == x):
                return int(middle)
            if(result > x):
                maximum = middle
            else:
                minimum = middle
        return int(maximum)
        
        