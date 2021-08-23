class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = ''
        for c in s:
            if c in ['{', '[', '(']:
                parentheses += c
            else:
                if len(parentheses) == 0:
                    return False
                elif c == '}' and '{' == parentheses[-1]:
                    parentheses = parentheses[:-1]
                elif c == ']' and '[' == parentheses[-1]:
                    parentheses = parentheses[:-1]
                elif c == ')' and '(' == parentheses[-1]:
                    parentheses = parentheses[:-1]
                else:
                    return False
        return len(parentheses) == 0