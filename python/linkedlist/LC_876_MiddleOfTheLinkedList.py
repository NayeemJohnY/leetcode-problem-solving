# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional
from linkedlist.listnode import ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head, fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        