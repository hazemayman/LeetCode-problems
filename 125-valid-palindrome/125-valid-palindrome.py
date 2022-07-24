class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        cleaned = ''
        for i in s:
            if(not(i in punctuations or i ==' ') ):
                cleaned += i.lower()
        print(cleaned)
        n = len(cleaned)
        for i in range(n // 2):
            if(cleaned[i] != cleaned[n - i -1]):
                return False
        return True