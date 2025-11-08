class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (!l1){
            return l2;
        }
        if (!l2){
            return l2;
        }
        ListNode* LinkedList = new ListNode();
        ListNode* pll = LinkedList;
        int temp = 0;
        short carry = 0;
        while (l1 || l2 || carry){
            if (l1){
                temp += l1->val;
                l1 = l1->next;
            }
            if (l2){
                temp += l2->val;
                l2 = l2->next;
            }
            temp += carry;
            LinkedList->next = new ListNode(temp%10);
            carry = temp / 10;
            LinkedList = LinkedList->next;
            temp = 0;
        }
        return pll->next;

    }
};
