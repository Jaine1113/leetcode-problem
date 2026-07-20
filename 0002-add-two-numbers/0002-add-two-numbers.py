class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next

        return dummy.next