class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for c in s:
            if c in ['{', '[', '(']:
                parentheses.append(c)
            else:
                if len(parentheses) == 0:
                    return False
                elif c == '}' and '{' == parentheses[-1]:
                    parentheses.pop()
                elif c == ']' and '[' == parentheses[-1]:
                    parentheses.pop()
                elif c == ')' and '(' == parentheses[-1]:
                    parentheses.pop()
                else:
                    return False
        return len(parentheses) == 0