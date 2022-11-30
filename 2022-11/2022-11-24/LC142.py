# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        connection = set()
        while head:
            pair = head
            if pair in connection:
                return pair
            else:
                connection.add(pair)
            head = head.next

        return None
