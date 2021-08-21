class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x == 0:
            return True
        n_digit = log10(x)//1
        i = 0
        while i < (n_digit+1)//2:
            n_i = (x//10**(n_digit-i))%10
            n_j = (x%10**(i+1))//10**i
            if n_i != n_j:
                return False
            else:
                i+=1
        return True