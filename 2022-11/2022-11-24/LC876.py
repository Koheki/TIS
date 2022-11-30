# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        N = 0
        count = head

        while count:
            N += 1
            count = count.next

        N //= 2
        while N > 0:
            head = head.next
            N -= 1

        return head