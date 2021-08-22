class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for banks in accounts:
            s = sum(banks)
            if s > maximum:
                maximum = s
        return maximum
            