/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // declare a third list node
        ListNode new_list = new ListNode(0);
        ListNode l3 = new_list;
        // declare carry just like in python
        int carry = 0;
        // then loop through the values in the nodes and declare them:
        while(l1!=null || l2!=null){
            int x =(l1!=null)?l1.val:0;
            int y =(l2!=null)?l2.val:0;
            int sum = x + y + carry; 
            
            // avoid any values with 0:
            carry = sum/10;
            int last_digit = sum%10;
            // create a temp list node to to store the new values:
            ListNode temp = new ListNode(last_digit);
            // connect the temp node with new node created earlier:
            l3.next = temp;
            l3 = l3.next;
            // then add the rest of the values to the new list
            if(l1!=null)
                l1 = l1.next;
            if(l2!=null)
                l2 = l2.next;
            
        }
        if(carry >0){
            ListNode temp = new ListNode(carry);
            l3.next = temp;
            // i guess we always have to leave the next value(possibility) open:
            l3 = l3.next;
            
        }
        return new_list.next;
            
    }
}