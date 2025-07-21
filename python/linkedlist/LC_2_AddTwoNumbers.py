# https://leetcode.com/problems/add-two-numbers

from typing import Optional
from linkedlist.listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        total = ListNode()
        current = total
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current.next = ListNode(sum % 10)
            carry = sum // 10
            current = current.next
        
        # while l1 or l2 or carry:
        #     sum = carry
        #     if l1:
        #         sum += l1.val
        #         l1 = l1.next
        #     if l2:
        #         sum + l2.val
        #         l2 = l2.next

        #     current.next = ListNode(sum % 10)
        #     carry = sum // 10
        #     current = current.next
            
        return total.next
    