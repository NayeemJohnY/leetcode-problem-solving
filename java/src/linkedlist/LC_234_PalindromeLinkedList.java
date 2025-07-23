package linkedlist;
// https://leetcode.com/problems/palindrome-linked-list
public class LC_234_PalindromeLinkedList {

    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null;
        ListNode curr = slow;
        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        fast = head;
        while (prev != null) {
            if (prev.val != fast.val)
                return false;
            prev = prev.next;
            fast = fast.next;
        }
        return true;
    }

    public static void main(String[] args) {
        ListNode node = new ListNode(1);
        node.next = new ListNode(2);
        node.next.next = new ListNode(2);
        node.next.next.next = new ListNode(1);

        LC_234_PalindromeLinkedList palindromeLinkedList = new LC_234_PalindromeLinkedList();
        System.out.println(palindromeLinkedList.isPalindrome(node));
    }
}