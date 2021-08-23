class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for c in s:
            if c in ['{', '[', '(']:
                parentheses.append(c)
            else:
                if not parentheses:
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