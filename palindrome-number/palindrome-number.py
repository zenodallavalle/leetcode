class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x < 10:
            return True
        rev_x = 0
        n_digit = log10(x) // 1
        for i in range(int(n_digit) + 1):
            rev_x += ((x//10**(n_digit-i))%10)*(10**i)
        return rev_x == x