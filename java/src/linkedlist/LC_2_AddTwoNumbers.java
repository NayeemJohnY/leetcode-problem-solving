package linkedlist;
// https://leetcode.com/problems/add-two-numbers

public class LC_2_AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode total = new ListNode();
        ListNode current = total;

        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int lVal1 = l1 != null ? l1.val : 0;
            int lVal2 = l2 != null ? l2.val : 0;
            int sum = lVal1 + lVal2 + carry;
            current.next = new ListNode(sum % 10);
            current = current.next;
            carry = sum / 10;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }

        return total.next;

    }
}
