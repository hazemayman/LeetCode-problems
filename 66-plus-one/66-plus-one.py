class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1 , -1 , -1):
            remainder = (digits[i] + 1)  // 10
            if(remainder): 
                digits[i] = 0
            else:
                digits[i]+=1
                break
        if(remainder):
            digits.insert(0 , 1)
        return digits