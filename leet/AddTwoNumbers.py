# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self is not None:
            print(self.val)
            self = self.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        ret = ListNode(0)
        head = ret
        while l1 is not None and l2 is not None:
            sumNum = l1.val + l2.val + flag
            if sumNum > 9:
                flag = 1
                head.next = ListNode(sumNum - 10)
            else:
                flag = 0
                head.next = ListNode(sumNum)
            head = head.next
            l1 = l1.next
            l2 = l2.next

        remain = None
        if l1 is not None:
            remain = l1
        elif l2 is not None:
            remain = l2
        
        while remain is not None:
            if flag == 0:
                head.next = remain
                break
            sumNum1 = remain.val + flag
            if sumNum1 > 9:
                flag = 1
                head.next = ListNode(sumNum1 - 10)
            else:
                flag = 0
                head.next = ListNode(sumNum1)
            head = head.next
            remain = remain.next

        if flag == 1:
            head.next = ListNode(1)

        return ret.next

l1 = ListNode(1)
l2 = ListNode(2)
solution = Solution()
l = solution.addTwoNumbers(l1,l2)
l.print()
