class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def hasPrefix(s:str, prefix:str)->bool:
            for i, c in enumerate(prefix):
                if i >= len(s):
                    return False
                if s[i] != c:
                    return False
            return True
        
        if len(strs)==1:return strs[0]
        
        j=1
        if strs[0] == '':
            return ''
        else:
            substring=strs[0][:j]
        
        while substring:
            i = 1
            while i<len(strs):
                if not hasPrefix(strs[i], substring):
                    return substring[:-1]
                i+=1
            if j == len(strs[0]):
                return substring
            j += 1
            substring = strs[0][:j]
        return ''