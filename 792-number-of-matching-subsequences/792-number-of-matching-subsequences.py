class Solution:
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lookup = defaultdict(list)
        for word in words:
            lookup[word[0]].append(word[1:])
        Counter = 0
        for charachter in s:
            if(charachter in lookup):
                word_remainder_list = lookup.pop(charachter)
                for word_remainder in word_remainder_list:
                    if(len(word_remainder) == 0):
                        Counter+=1
                    else:
                        lookup[word_remainder[0]].append(word_remainder[1:])

        return Counter