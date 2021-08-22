# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        results = []
        def sum(x, y, prev_r=0):
            summed = x.val + y.val + prev_r
            r = 0
            if summed > 9:
                r += 1
                summed -= 10
            results.append(summed)
            # result = ListNode(summed, next=res)
            if (not x.next) and (not y.next) and (not r):
                return
            else:
                return sum(x.next or ListNode(0, None), y.next or ListNode(0, None), r)
        sum(l1, l2)
        result = None
        for r in reversed(results):
            result = ListNode(r, result)
        return result
            