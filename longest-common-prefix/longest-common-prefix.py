class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def hasPrefix(s:str, prefix:str)->bool:
            for i, c in enumerate(prefix):
                if i >= len(s):
                    return False
                if s[i] != c:
                    return False
            return True
        strs = sorted(strs, key=len)
        substring = strs[0]
        while substring:
            if all(map(lambda x: hasPrefix(x, substring), strs)):
                return substring
            substring = substring[:-1]
        return ''