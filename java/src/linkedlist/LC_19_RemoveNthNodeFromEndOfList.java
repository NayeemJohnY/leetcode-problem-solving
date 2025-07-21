package linkedlist;
// https://leetcode.com/problems/remove-nth-node-from-end-of-list

public class LC_19_RemoveNthNodeFromEndOfList {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode slow = dummy, fast = head;
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }

        if (slow.next != null)
            slow.next = slow.next.next;

        return dummy.next;
    }
}
