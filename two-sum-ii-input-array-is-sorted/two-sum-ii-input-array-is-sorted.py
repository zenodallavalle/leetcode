class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        previous = {}
        i = 0
        while i < len(numbers):
            element = numbers[i]
            delta = target - element
            if delta in previous:
                return previous[delta] + 1, i + 1
            else:
                previous[element] = i
            i += 1