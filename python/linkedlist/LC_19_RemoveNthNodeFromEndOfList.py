# https://leetcode.com/problems/remove-nth-node-from-end-of-list

from typing import Optional
from linkedlist.listnode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if slow.next:
            slow.next = slow.next.next
        return dummy.next
