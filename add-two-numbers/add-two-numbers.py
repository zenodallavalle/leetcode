# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def sum(x, y, result=None, res=None, prev_residual=0):
            summed = x.val + y.val + prev_residual
            residual = 0
            if summed > 9:
                residual += 1
                summed -= 10
            if not result:
                result = res = ListNode(summed)
            else:
                res.next = ListNode(summed)
                res = res.next
            if (not x.next) and (not y.next) and (not residual):
                return result
            else:
                return sum(x.next or ListNode(), y.next or ListNode(), result, res, residual)
        return sum(l1, l2)