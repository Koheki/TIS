# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode(-1)
        tmp = res
        while head != None:
            tmp.next = ListNode(head)
            head = head.next
            tmp = tmp.next

        return res