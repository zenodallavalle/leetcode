class Solution:
    def myAtoi(self, s: str) -> int:
        number = 0
        found_valid_chars = False
        negative = None
        i = 0
        while i < len(s):
            c = s[i]
            if '0' <= c <= '9':
                found_valid_chars = True
                if not negative:
                    if number <= (2**31-1-int(c))/10:
                        number = number*10 + int(c)
                    else:
                        return 2**31-1
                else:
                    if number >= (-2**31+int(c))/10:
                        number = number *10 - int(c)
                    else:
                        return -2**31
            else:
                if found_valid_chars:
                    # Didn't recognized a number and already removed leading ' ' so break it
                    break
                elif c == '+':
                    negative = False
                    found_valid_chars = True
                elif c == '-':
                    negative = True
                    found_valid_chars = True
                elif c == ' ':
                    pass
                else:
                    break
            i+=1
        return number