class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 : return 0
        if x == 1 : return 1
        minimum = 1
        maximum = x
        div = 10
        while(div > 1):
            temp = maximum / div
            if(temp * temp <= x+1):
                div-=1
            else:
                maximum = temp
                
        
        
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
        
        