package linkedlist;

// https://leetcode.com/problems/reverse-linked-list-ii
public class LC_92_ReverseLinkedListII {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left > right)
            return head;

        ListNode dummyNode = new ListNode();
        dummyNode.next = head;
        ListNode prev = dummyNode;

        for (int i = 1; i < left; i++) {
            prev = prev.next;
            if (prev == null)
                return head;
        }

        ListNode curr = prev.next;
        for (int j = 0; j < right - left; j++) {
            ListNode temp = curr.next; // temp = 3 -> 4
            curr.next = temp.next; // 2 -> 3 => 2 -> 4
            temp.next = prev.next; // 3 -> 4 => 3 -> 2
            prev.next = temp; // 1 -> 2 => 1 -> 3
        }

        return dummyNode.next;
    }
}
