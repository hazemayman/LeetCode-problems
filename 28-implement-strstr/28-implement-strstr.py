class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle) == 0) : return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                condition = True
                for j in range(1 , len(needle)):
                    if(needle[j] != haystack[i+j]):
                        condition = False
                        break
                if(condition):return i
        return -1