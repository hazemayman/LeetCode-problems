class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        s = s.strip()
        for i in range(len(s)-1 , -1 , -1):
            if(s[i] == " "):break
            ans+=1
        return ans 
            