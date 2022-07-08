lookuptable = None

def initialize(ls1 , ls2):
    global lookuptable
    lookuptable = [[-1 for i in range(ls2+1)] for j in range(ls1+1)]

class Solution:
    
    def rec(self , s1 ,s2 ,s3):
        length_s1 = len(s1)
        length_s2 = len(s2)
        length = len(s3)
        
        if(length != length_s1 + length_s2):
            return False
        elif(length == 0):
            return True
        
        if(lookuptable[length_s1][length_s2] != -1): return lookuptable[length_s1][length_s2]
        s1Condition = s2Condition = False
        if(len(s2) > 0 and s3[-1] == s2[-1]):
            s2Condition = True
        if(len(s1) > 0 and s3[-1] == s1[-1]):
            s1Condition = True
        
        if(s1Condition and s2Condition):
            lookuptable[length_s1][length_s2] = self.rec(s1[:-1] , s2 , s3[:-1]) or self.rec(s1, s2[:-1] , s3[:-1]) 
        elif(s1Condition):
            lookuptable[length_s1][length_s2] = self.rec(s1[:-1] , s2 , s3[:-1]) 
        elif(s2Condition):
            lookuptable[length_s1][length_s2] = self.rec(s1, s2[ : -1] , s3[:-1]) 
        else:
            lookuptable[length_s1][length_s2] = False 
        return  lookuptable[length_s1][length_s2]
        
            
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
      
        initialize(len(s1)  ,len(s2))
        return self.rec(s1 , s2 , s3)
        