/**
 * Problem asks 
 */


public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast, slow;
        fast = slow = head;
        while (fast != null){
            if (fast.next == null){
                return false;
            }
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow){
                return true;
            }

        }

        return false;
    }
}