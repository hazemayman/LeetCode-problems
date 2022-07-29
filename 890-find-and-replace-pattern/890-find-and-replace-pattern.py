class Solution:

    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match (word):
            wordLookup, patternLookup = {},{}
            for w , p in zip(word , pattern):
                if w not in wordLookup : wordLookup[w] = p
                if p not in patternLookup: patternLookup[p] = w
                if((patternLookup[p],wordLookup[w]) != (w,p)):
                    return False
            return True

        return list(filter(match , words))
