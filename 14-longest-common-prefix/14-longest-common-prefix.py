class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 1): return strs[0]
        comparison = strs[0]
        points = [0 for i in range(len(strs) - 1)]
        for i in range(1 , len(strs)):
            counter = 0
            try:
                for j in range(len(comparison)):
                    if(comparison[j] == strs[i][j]):
                        counter+=1
                    else:
                        break
            except:
                pass
            points[i-1] = counter

        try:
            return  comparison[0:min(points)]
        except:
            return ""
            
            