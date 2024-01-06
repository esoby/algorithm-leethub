# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = ListNode(0)
        odd_p = odd
        even = ListNode(0)
        even_p = even

        cnt = 1

        while head:
            
            if cnt % 2:
                # 홀수
                odd_p.next = head
                odd_p = odd_p.next
            else:
                # 짝수 
                even_p.next = head
                even_p = even_p.next

            head = head.next
            cnt += 1
        
        even_p.next = None
        odd_p.next = even.next

        return odd.next