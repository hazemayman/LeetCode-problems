class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        lookup = {}
        for i in s:
            if i in lookup:
                lookup[i]+=1
            else:
                lookup[i] = 1
        
        for j in t:
            if j in lookup:
                if lookup[j] > 1:
                    lookup[j]-=1
                else:
                    del lookup[j]
            else:
                return False
        for i in lookup:
            return False
        return True