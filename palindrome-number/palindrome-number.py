class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
        if x < 0: return False
        elif x == 0: return True
        
        div = 10 ** (log10(x)//1)
        
        # div = 1
        # while x >= 10*div:
        #     div *= 10
        
        while x:
            # right = x % 10
            # left = x//div
            
            if (x % 10) != (x//div): return False
            
            x = (x % div) // 10
            div /= 100
        return True