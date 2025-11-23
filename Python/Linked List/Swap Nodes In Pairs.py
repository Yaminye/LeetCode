# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        one = head
        two = head.next
        three = head.next.next
        head = head.next
        h = ListNode(next = one)
        while True:
            two.next = one
            one.next = three
            h.next = two
            for i in range(2):
                if not three:
                    return head
                three = three.next
                two = two.next
                one = one.next
                h = h.next
            temp = one
            one = two
            two = temp
        return head
