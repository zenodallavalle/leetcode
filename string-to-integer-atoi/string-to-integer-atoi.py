class Solution:
    def myAtoi(self, s: str) -> int:
        
        def checkOverflow(x: int) -> int:
            if x > (2**31-1):
                return 2**31 - 1
            elif x < (-2**31):
                return -2**31
            return x
        
        digits = '0'
        for c in s:
            if digits != '0':
                if '0'<=c<='9':
                    digits += c
                else:
                    return checkOverflow(int(digits))
            else:
                if c == '+' or c == '-':
                    digits = c + digits
                elif '0' <= c <= '9':
                    digits += c
                elif c == ' ':
                    pass
                else:
                    return checkOverflow(int(digits))
        return checkOverflow(int(digits))