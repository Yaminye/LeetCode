class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        pre = ListNode(next=head)

        for i in range(n):
            if not head:
                break    
            head = head.next
        temp = pre
        while(head):
            head = head.next
            temp = temp.next
        temp.next = temp.next.next
        return pre.next
