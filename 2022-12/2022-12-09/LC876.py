# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = head
        c = 0
        while count:
            c += 1
            count = count.next

        for _ in range(c//2):
            head = head.next

        return head