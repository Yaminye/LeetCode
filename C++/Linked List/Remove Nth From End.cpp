class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head){
            return head;
        }
        ListNode* res = head;
        ListNode* prev = head;
        ListNode* temp = head;
        int i = 0;
        while(i < n && head){
            head = head->next;
            i++;
        }
        if (i < n){
            return res;
        }
        if (!head) {
            return res->next;
        }

        while(head){
            temp = prev;
            prev = prev->next;
            head = head->next;
        }
        if (prev){
            temp->next = prev->next;
            prev->next = nullptr;
        }
        return res;

    }
};
