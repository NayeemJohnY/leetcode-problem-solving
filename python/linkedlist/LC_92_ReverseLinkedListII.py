#  https://leetcode.com/problems/reverse-linked-list-ii
from typing import Optional
from linkedlist.listnode import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left > right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = head
        for _ in range(1, left):
            prev = prev.next
            if prev is None:
                return head
        
        curr = prev.next
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev = temp
        
        return dummy.next