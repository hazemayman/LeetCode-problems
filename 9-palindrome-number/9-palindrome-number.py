class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False
        number = str(x)
        l = len(number)
        for i in range(0 , l // 2):
            if(number[i] != number[l - i - 1]):
                return False
        return True
        
        