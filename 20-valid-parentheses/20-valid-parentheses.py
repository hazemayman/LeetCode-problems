

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for c in s :
            if c in p.keys():
                stack.append(c)
            else:
                if(len(stack) == 0 ): return False
                if(p[stack[-1]] == c):
                    stack.pop()
                else:
                    return False
        if(len(stack) == 0): return True
        return False
        