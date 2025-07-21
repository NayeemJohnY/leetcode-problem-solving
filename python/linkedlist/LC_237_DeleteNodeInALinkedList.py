# https://leetcode.com/problems/delete-node-in-a-linked-list

from typing import Optional
from linkedlist.listnode import ListNode


class Solution:
    def deleteNode(self, node: Optional[ListNode]):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
