# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result={}
        def sum(x, y, res=None, prev_r=0):
            summed = x.val + y.val + prev_r
            r = 0
            if summed > 9:
                r += 1
                summed -= 10
            if not 'result' in result:
                result['result'] = ListNode(summed)
                res = result['result']
            else:
                res.next = ListNode(summed)
                res = res.next
            if (not x.next) and (not y.next) and (not r):
                return result
            else:
                return sum(x.next or ListNode(0, None), y.next or ListNode(0, None), res, r)
        sum(l1, l2)
        return result['result']