class Solution:
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lookup = {}
        for i in range(len(s)):
            if s[i] in lookup:
                lookup[s[i]].append(i)
            else:
                lookup[s[i]] = [i]
                
        Counter = 0
        while(len(words) > 0):
            word = words.pop()
            index = -1
            condition = True
            for i in range(0 , len(word)):
                if(word[i] in lookup):
                    innerCondition = False
                    for raw_index in lookup[word[i]]:
                        if(raw_index > index):
                            index = raw_index
                            innerCondition = True
                            break
                    if(not innerCondition):
                        condition = False
                        break
                        
                else:
                    condition = False
                    break
            if(condition):
                
                Counter+=1
                
        return Counter