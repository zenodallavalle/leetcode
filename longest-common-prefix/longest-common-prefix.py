class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # strs = sorted(strs, key=len)
        substring = strs[0]
        
        def repeat(substring:str):
            while True:
                yield substring
        
        def hasPrefix(s:str, prefix:str)->bool:
            for i, c in enumerate(prefix):
                if i >= len(s):
                    return False
                if s[i] != c:
                    return False
            return True
        
        while substring:
            if all(map(hasPrefix, strs, repeat(substring))):
                return substring
            substring = substring[:-1]
        return ''