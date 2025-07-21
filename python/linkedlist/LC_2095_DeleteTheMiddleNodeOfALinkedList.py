# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

from typing import Optional
from linkedlist.listnode import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = head
        if head.next:
            fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
