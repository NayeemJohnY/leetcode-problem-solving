# https://leetcode.com/problems/palindrome-linked-list
from typing import Optional
from linkedlist.listnode import ListNode

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev, curr  = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        fast = head
        while prev:
            if fast.val != prev.val:
                return False
            fast = fast.next
            prev = prev.next
        return True
    
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(sol.isPalindrome(head))
    

